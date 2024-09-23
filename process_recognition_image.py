import json

from PIL import Image, ImageEnhance, ImageDraw
from auxiliary_funcs import get_current_time
import numpy as np
import easyocr


class RecognitionProcessingImage:

    def __init__(self, image_path):
        self.errors = []  # List of errors (time, str)

        self.image_path = image_path
        self.before_image = None  # To draw recognized text
        self.__load_image()
        # Open and read the JSON (settings) file
        with open('Settings/cur_settings.json', 'r') as file:
            data = json.load(file)
        save_path_dir = data["save_path"]["for_image"]
        self.save_path = save_path_dir + self.image_path.split("/")[-1].split(".")[0]

    def __load_image(self):
        try:
            self.image = Image.open(self.image_path)
            self.before_image = self.image.copy()
        except FileNotFoundError:
            self.errors.append((get_current_time(), "This file does not exist!"))
            self.image = None
        except Exception:
            self.errors.append((get_current_time(), "An error occurred in the loading of the image"))

    def change_size(self):
        width, height = self.image.width, self.image.height
        # Change the image size (if necessary)
        self.image = self.image.resize((int(width * 1.4), int(height * 1.4)), Image.LANCZOS)
        self.before_image = self.image.copy()  # Save the original scale image

    def convert_to_gray(self):
        """Convert the image to grayscale"""
        self.image = self.image.convert("L")

    def change_contrast(self):
        """Change the contrast"""
        enhancer = ImageEnhance.Contrast(self.image)
        self.image = enhancer.enhance(1.75)  # Increase contrast by 75%

    def change_threshold(self):
        """Change the threshold"""
        self.image = self.image.point(lambda p: 255 if p > 128 else 0)

    def invert_color(self):
        """Invert the color"""
        self.image = Image.eval(self.image, lambda p: 255 - p)

    @property
    def preprocess_image(self):
        """Preparatory image processing"""
        self.change_size()
        self.convert_to_gray()
        self.change_contrast()
        self.change_threshold()
        self.invert_color()
        return self.image

    def get_text(self):
        """Recognize text in the image"""
        processed_img = self.preprocess_image  # Convert image

        # Convert image to NumPy array for EasyOCR
        img_np = np.array(processed_img)

        # Initialize EasyOCR
        reader = easyocr.Reader(['ru'], gpu=True)

        # Recognize text, get results
        results = reader.readtext(img_np)
        res_text = ""

        # Get text from results
        for detection in results:
            res_text += detection[1] + "\n"
            bbox = detection[0]  # The borders of the recognized block
            try:
                self.draw_borders_on_image(bbox)
            except Exception:
                self.errors.append((get_current_time(), "An error occurred in the drawing of the borders"))
        return res_text

    def convert_to_TXT(self, text):
        """Converts the image to .txt format."""
        with open(self.save_path + ".txt", "w", encoding="utf-8") as file:
            file.write(text)

    @property
    def recognize_text(self):
        """Main function to recognize"""
        res_text = self.get_text()
        try:
            self.convert_to_TXT(res_text)
        except FileNotFoundError:
            self.errors.append((get_current_time(), "The directory not found!"))  # Directory not found
        except PermissionError:
            self.errors.append((get_current_time(), "No permission to create a file"))  # No permission to create a file
        except OSError as e:
            self.errors.append((get_current_time(), "An error occurred in the OS"))  # An error occurred
        return res_text, self.errors

    def draw_borders_on_image(self, border):
        """Draw the borders of the recognized text"""
        draw = ImageDraw.Draw(self.before_image)
        left_top = list(map(int, border[0]))
        right_bottom = list(map(int, border[2]))
        ltx, lty, rbx, rby = left_top[0], left_top[1], right_bottom[0], right_bottom[1]
        # Swap the coordinates if necessary
        if ltx > rbx:
            ltx, rbx = rbx, ltx
        if lty > rby:
            lty, rby = rby, lty
        draw.rectangle([ltx, lty, rbx, rby], fill=None,
                       outline=(255, 0, 0), width=3)  # Draw the borders on the image
