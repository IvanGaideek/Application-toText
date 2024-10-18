# Application: toText 
[![License](https://img.shields.io/badge/License-AGNU-brightgreen.svg)](https://github.com/IvanGaideek/Application-toText/tree/master/LICENSES) ![Static Bradge](https://img.shields.io/badge/python-v3.9-blue?style=flat&logo=python) ![Static Badge](https://img.shields.io/badge/version%201.1-yellow?style=plastic&logo=sessionize&logoColor=%231AB394) [![Setup app](https://img.shields.io/badge/Setup%20app-Click%20Here-brightgreen.svg)](https://disk.yandex.ru/d/VL0ixTYBCA7O_g)
 --- ![alt text](https://github.com/IvanGaideek/Application-toText/blob/master/Design/main_icon.svg)
## Libraries that helped make the project❤️:
![Static Badge](https://img.shields.io/badge/PyTorch-blue?style=for-the-badge&logo=pytorch&logoColor=%23EE4C2C&link=https%3A%2F%2Fgithub.com%2FIvanGaideek%2FApplication-toText%2Fblob%2Fmaster%2FLICENSES%2FLICENSE) ![Static Badge](https://img.shields.io/badge/PyMuPDF-green?style=for-the-badge) ![Static Badge](https://img.shields.io/badge/PySide6-orange?style=for-the-badge&logo=qt&logoColor=%2341CD52) ![Static Badge](https://img.shields.io/badge/Pillow-gray?style=for-the-badge) ![Static Badge](https://img.shields.io/badge/easyocr-brown?style=for-the-badge) ![Static Badge](https://img.shields.io/badge/pdf2docx-violet?style=for-the-badge) ![Static Badge](https://img.shields.io/badge/openai--whisher-red?style=for-the-badge&logo=openai&logoColor=%23412991)
------------------------
## The main functions of the application:
- Optical text recognition (OCR) from images.
- Speech recognition from audio files.
- Convert PDF files to text documents, extract images and tables
### Installing the application
Link to the installer file archive: [Yandex.disk](https://disk.yandex.ru/d/VL0ixTYBCA7O_g "application toText")
### About the launch
Install the libraries using the command:
```
pip install -r requirements.txt
```
The file to run is main.py - main.py\
Files with information about the application in the [docs](https://github.com/IvanGaideek/Application-toText/tree/master/docs) folder.\
The settings are stored in JSON files, which are located in [Settings](https://github.com/IvanGaideek/Application-toText/tree/master/Settings)
### Additional information and notes:
The weight of the final application is ~288 Mb
But during recognition, language sets and recognition models (in speech recognition) will be downloaded to your computer as needed.
Unfortunately, version 1.1 has almost no GPU support.
The ffmpeg package must be installed for speech recognition to work, if it is not installed.
