from PySide6.QtWidgets import QSplashScreen, QProgressBar
from PySide6.QtGui import QMovie, QPixmap, QPainter, QPainterPath
from PySide6.QtCore import QSize


class MovieSplashScreen(QSplashScreen):
    my_size = QSize(1000, 600)  # Initial size of the splash screen

    def __init__(self, path_to_gif: str, progressbar_value: int):
        self.movie = QMovie(path_to_gif)  # Path to the gif: main splash screen
        self.movie.jumpToFrame(0)

        pixmap = QPixmap(self.my_size)
        super().__init__(pixmap)
        self._set_rounded_square_mask()

        self.progressbar = QProgressBar(self)
        self.progressbar.setStyleSheet("QProgressBar {border: 2px solid #2196F3; border-radius: 5px;"
                                       " background-color: #F2F2F2;}"
                                       " QProgressBar::chunk {background-color: #2197F3; width: 10px; margin: 0.5px;}")
        self.progressbar.setMaximum(progressbar_value)
        self.progressbar.setTextVisible(False)
        self.progressbar.setGeometry(0, self.my_size.height() - 50, self.my_size.width(), 20)

        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, event):
        self.movie.start()

    def hideEvent(self, event):
        self.movie.stop()

    def paintEvent(self, event):
        """Paint the gif in the splash screen"""
        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        pixmap = pixmap.scaled(self.my_size)
        painter.drawPixmap(0, 0, pixmap)

    def update_progress(self, value):
        self.progressbar.setValue(value)

    def _set_rounded_square_mask(self):
        # Creating rounded rectangles
        corner_radius = 20
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.my_size.width(), self.my_size.height(), corner_radius, corner_radius)
        self.setMask(path.toFillPolygon().toPolygon())  # Instantiate the mask
