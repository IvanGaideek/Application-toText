import json
import os

import fitz  # PyMuPDF
from pdf2docx import Converter
from auxiliary_funcs import get_current_time
import csv


class RecognitionProcessingPDF:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        # Open and read the JSON (settings) file
        with open('Settings/cur_settings.json', 'r') as file:
            data = json.load(file)
        save_path = data["save_path"]["for_pdf"]
        self.create_save_directories(save_path)
        self.errors = []  # List of errors (time, str)

    def create_save_directories(self, directory):
        self.name_save_one_pdf = self.pdf_path.split(".")[0].split("/")[-1]  # the directory of files of one PDF
        self.path_save_one = directory + self.name_save_one_pdf
        if not os.path.isdir(self.path_save_one):
            os.makedirs(self.path_save_one)
        dir_list = ["tables", "images"]  # the directories of files of one PDF
        for dir in dir_list:
            if not os.path.isdir(self.path_save_one + "/" + dir):
                os.makedirs(self.path_save_one + "/" + dir)

    @property
    def recognize(self):
        """Determines by settings what needs to be extracted from the PDF file"""
        text = self.recognize_text()
        self.error_correction(self.save_tables, "The problem with the encoding of the table",
                              "The problem with the permission of the dir for table")
        self.error_correction(self.convert_to_TXT, "The problem with the encoding of the text",
                              "The problem with the permission of the dir for text")
        self.error_correction(self.save_images, "The problem with the encoding of the image",
                              "The problem with the permission of the dir for image")
        self.error_correction(self.convert_to_WORD, "The problem with the encoding of the word",
                              "The problem with the permission of the dir for word")
        return text, self.errors

    def error_correction(self, func, mes_unicode, mes_permission):
        try:
            func()  # Execute the function
        except UnicodeEncodeError:
            self.errors.append((get_current_time(), mes_unicode))
        except PermissionError:
            self.errors.append((get_current_time(), mes_permission))

    def convert_to_WORD(self):
        # Create a Converter object
        cv = Converter(self.pdf_path)

        # Converting the specified PDF page to docx
        cv.convert(self.path_save_one + "/" + self.name_save_one_pdf + ".docx", start=0, end=None)
        cv.close()

    def convert_to_TXT(self):
        """Converts the PDF file to .txt format."""
        with open(self.path_save_one + "/" + self.name_save_one_pdf + ".txt", "w", encoding="utf-8") as file:
            file.write(self.recognize_text())

    def save_images(self):
        with fitz.open(self.pdf_path) as file:
            # iterate over PDF pages
            for page_index in range(len(file)):
                # get the page itself
                page = file.load_page(page_index)  # load the page
                image_list = page.get_images(full=True)  # get images on the page

                for image_index, img in enumerate(image_list, start=1):
                    # get the XREF of the image
                    xref = img[0]

                    # extract the image bytes
                    base_image = file.extract_image(xref)
                    image_bytes = base_image["image"]

                    # get the image extension
                    image_ext = base_image["ext"]

                    # save the image
                    image_name = self.path_save_one + "/images/" + f"{page_index}_{image_index}.{image_ext}"
                    with open(image_name, "wb") as image_file:
                        image_file.write(image_bytes)

    def save_tables(self):
        with fitz.open(self.pdf_path) as file:
            for n, page in enumerate(file):
                tabs = page.find_tables()
                if tabs.tables:
                    self.write_to_csv(tabs[0].extract(), n)

    def write_to_csv(self, array, page):
        with open(self.path_save_one + "/tables/" + str(page) + ".csv", "w", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";", quoting=csv.QUOTE_ALL)
            for row in array:
                writer.writerow(row)

    def recognize_text(self):
        with fitz.open(self.pdf_path) as file:
            text = ""
            for page in file:  # Iterate through the pages
                text += page.get_text()

            return text
