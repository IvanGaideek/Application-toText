import fitz  # PyMuPDF
import csv


class RecognitionProcessingPDF:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    @property
    def recognize(self):
        """Determines by settings what needs to be extracted from the PDF file"""
        text = self.recognize_text()
        # self.save_tables()
        # self.convert_to_TXT()
        # self.save_images()
        return text

    def convert_to_WORD(self):
        pass

    def convert_to_TXT(self):
        """Beta: Converts the PDF file to .txt format."""
        with open(self.pdf_path.split(".")[0] + ".txt", "w") as file:
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
                    image_name = "/".join(self.pdf_path.split("/")[:-1]) + "/" + f"{page_index}_{image_index}.{image_ext}"
                    with open(image_name, "wb") as image_file:
                        image_file.write(image_bytes)


    # Beta: recognize tables from PDF file
    def save_tables(self):
        with fitz.open(self.pdf_path) as file:
            for n, page in enumerate(file):
                try:
                    tabs = page.find_tables()
                    if tabs.tables:
                        self.write_to_csv(tabs[0].extract(), n)
                except UnicodeEncodeError:
                    pass

    def write_to_csv(self, array, page):
        with open(self.pdf_path.split(".")[0] + "_" + str(page) + ".csv", "w") as file:
            writer = csv.writer(file, delimiter=";", quoting=csv.QUOTE_ALL)
            for row in array:
                writer.writerow(row)
    ###############################

    def recognize_text(self):
        with fitz.open(self.pdf_path) as file:
            text = ""
            for page in file:  # Iterate through the pages
                text += page.get_text()

            return text
