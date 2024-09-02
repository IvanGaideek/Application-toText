from PySide6.QtWidgets import QApplication
from frontPage import MainWindow
import sys

# Create the Qt Application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
