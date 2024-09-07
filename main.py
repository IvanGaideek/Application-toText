from PySide6.QtWidgets import QApplication
from frontPage import MainWindow
import sys

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
