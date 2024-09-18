from PySide6.QtWidgets import QApplication
from frontPage import MainWindow
from auxiliary_funcs import work_begin_window
import sys

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    splash = work_begin_window(app)  # Create the splash screen
    window = MainWindow()
    window.show()
    splash.finish(window)
    app.exec()
