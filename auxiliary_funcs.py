import time

from PySide6.QtGui import QFontMetrics
from PySide6.QtWidgets import QLabel, QApplication

from splash_begin import MovieSplashScreen
from operation_with_settings import get_settings_for_splash


def check_file_extension(filename, valid_extensions):
    """Check if a file has a valid extension"""
    valid_extensions = valid_extensions[1:].split(" *")
    return any(filename.lower().endswith(ext) for ext in valid_extensions)


def read_file(plain_text_edit, full_name_file):
    with open(full_name_file, "r", encoding="utf-8") as file:
        plain_text_edit.setPlainText(file.read())  # write to the widget


def wrap_text(your_label: QLabel):
    text = your_label.text()
    max_message_width = your_label.width()
    message_metrics = QFontMetrics(your_label.font())
    side_margins = your_label.contentsMargins().right() + your_label.contentsMargins().left()

    cur_len = 0
    pos = 0

    while pos < len(text):
        ch = text[pos]
        if ch == ' ' or ch == '\n' or ch == '_' or ch == '-':
            cur_len = 0
        else:
            cur_len += message_metrics.horizontalAdvance(ch)
            if cur_len > (max_message_width - side_margins - 40):
                text = text[:pos] + '\n' + text[pos:]  # Insert a newline character
                cur_len = 0
        pos += 1

    your_label.setText(text)  # Set the wrapped text back to the label


def work_begin_window(app: QApplication):
    """The boot window at the beginning of the application launch"""
    path_to_gif, progressbar_value = get_settings_for_splash()

    splash = MovieSplashScreen(path_to_gif, progressbar_value)
    splash.show()

    for i in range(progressbar_value):
        splash.update_progress(i)
        t = time.time()
        while time.time() < t + 0.04:
            app.processEvents()

        time.sleep(0.1)  # Adjust sleep time if needed

    return splash


def clear_result(your_label: QLabel):
    your_label.setText("")
