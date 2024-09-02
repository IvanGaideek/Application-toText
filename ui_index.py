# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_des.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1125, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1125, 650))
        MainWindow.setStyleSheet(u"QWidget\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0.100962 rgba(34, 166, 178, 255),stop:0.543269 rgba(132, 213, 51, 255),stop:1 rgba(208, 255, 163, 255));\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"	selection-background-color: #3b7e48;\n"
"\n"
"}\n"
"\n"
"#label_select_pdf_file, #label_image, #label_select_audio_file {\n"
"	border-radius: 10%;\n"
"	background-color: rgba(0, 173, 26, 70);\n"
"}\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel::disabled\n"
"{\n"
"	background-color: transparent;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0.100962 rgba(34, 166, 178, 255),stop:1 rgba(24, 123, 132, 255));\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #65"
                        "6565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background-color: #5ab8a0;\n"
"    border: 1px solid #41cd52;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background-color: #3e7f6e;\n"
"    border: 1px solid #5ab8a0;\n"
"    margin-bottom: -1px;\n"
"    padding-bottom: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #1f2b2b;\n"
"    border: 1px solid;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #22af00;\n"
"    color: #ffffff;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    min-width : 150px;\n"
"    padding: 3px 20px 3px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #22a6b2;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"Q"
                        "Menu::item:disabled\n"
"{\n"
"    color: #262626;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolTip-----*/\n"
"QToolTip\n"
"{\n"
"	border : 1px solid #000000;\n"
"	background-color: #26264f;\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: #20afe7;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 11px;\n"
"	border-color: #2082ff;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #33bdff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 11px;\n"
"	border-color: #2082ff;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #2082ff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 11px;\n"
""
                        "	border-color: #2082ff;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"	background-color: #20afe7;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 11px;\n"
"	border-color: #2082ff;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"	background-color: #33bdff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 11px;\n"
"	border-color: #2082ff;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"	background-color: #2082ff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 11px;\n"
"	border-color: #2082ff;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: #a9a9aa;\n"
"    border: 1px solid;\n"
"    paddin"
                        "g-left: 6px;\n"
"    color: #000;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:hover\n"
"{\n"
"    background-color: #f6f6f6;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #f8f6f0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #488f44;\n"
"    selection-color: #ffffff;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	background-color: #383838;	\n"
"    image: url(://arrow-down.png) 16px 16px;\n"
"    width: 18px;\n"
"    height: 18px;\n"
"	border-left: 1px solid black;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox & QDoubleSpinBox & QDat"
                        "eTimeEdit-----*/\n"
"QSpinBox, \n"
"QDoubleSpinBox,\n"
"QDateTimeEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color: #000;\n"
"	border: 1px solid #a9a9aa;\n"
"	padding : 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled, \n"
"QDoubleSpinBox::disabled,\n"
"QDateTimeEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox:hover, \n"
"QDoubleSpinBox::hover,\n"
"QDateTimeEdit::hover\n"
"{\n"
"    background-color: #a9a9aa;\n"
"    border: 1px solid #a9a9aa;\n"
"    color:  #000;\n"
"    padding: 2px\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button,\n"
"QDateTimeEdit::up-button, QDateTimeEdit::down-button\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0.100962 rgba(34, 166, 178, 255),stop:0.543269 rgba(132, 213, 51, 255),stop:1 rgba(208, 255, 163, 255));\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled, \n"
"QDoubleSpi"
                        "nBox::disabled,\n"
"QDateTimeEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover,\n"
"QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover,\n"
"QDateTimeEdit::up-button:hover, QDateTimeEdit::down-button:hover\n"
"{\n"
"    background-color: #92dd48;\n"
"    border: 1px solid #92dd48;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:disabled, QSpinBox::down-button:disabled,\n"
"QDoubleSpinBox::up-button:disabled, QDoubleSpinBox::down-button:disabled,\n"
"QDateTimeEdit::up-button:disabled, QDateTimeEdit::down-button:disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed,\n"
"QDoubleSpinBox::up-button:pressed, QDoubleSpinBox::down-button::pressed,\n"
"QDateTimeEdit::up-button:pressed, QDateTimeEdit::down-button::pressed\n"
"{\n"
"    background-color: #"
                        "57a951;\n"
"    border: 1px solid #57a951;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow,\n"
"QDateTimeEdit::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow,\n"
"QDateTimeEdit::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color: #000;\n"
"	border-width: 1px;\n"
"	border-radius: 0px;\n"
"	border-color: #051a39;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit::hover\n"
"{\n"
"	background-color: #a9a9aa;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTextEdit-----*/\n"
"QTextEdit, QPlainTextEdit\n"
"{\n"
"	background-color: rgba(221, 230, 255, 1"
                        "70);\n"
"	color: #010201;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border: 1px inset rgba(0, 0, 0, 20);\n"
"    border-top-right-radius: 3px;  /* \u0412\u0435\u0440\u0445\u043d\u0438\u0439 \u043f\u0440\u0430\u0432\u044b\u0439 \u0443\u0433\u043e\u043b */\n"
"    border-bottom-right-radius: 5px;/* \u041d\u0438\u0436\u043d\u0438\u0439 \u043f\u0440\u0430\u0432\u044b\u0439 \u0443\u0433\u043e\u043b */\n"
"    border-bottom-left-radius: 5px;  /* \u041d\u0438\u0436\u043d\u0438\u0439 \u043b\u0435\u0432\u044b\u0439 \u0443\u0433\u043e\u043b */\n"
"    margin-top: 22px;\n"
"	margin-left: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: rgba(0, 0, 0, 20);\n"
"	border: 1px inset rgba(0, 0, 0, 20);\n"
"    border-top-left-radius: 10px;   /* \u0412\u0435\u0440\u0445\u043d\u0438\u0439 \u043b\u0435\u0432\u044b\u0439 \u0443\u0433\u043e\u043b */\n"
"    border-top-right-radius: 10px;  /* \u0412\u0435\u0440"
                        "\u0445\u043d\u0438\u0439 \u043f\u0440\u0430\u0432\u044b\u0439 \u0443\u0433\u043e\u043b */\n"
"    color: #ffffff;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"	margin-left: 1px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #1f2b2b;\n"
"    border: 1px solid #2aaaa8;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(://checkbox.png);\n"
"	background-color: #1f2b2b;\n"
"    border: 1px solid #2aaaa8;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #2aaaa8;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:"
                        "disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton\n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked\n"
"{ \n"
"	border: 1px inset gray; \n"
"	border-radius: 5px; \n"
"	background-color:  #a9a9aa;\n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover\n"
"{ \n"
"	border: 1px inset #2aaaa8; \n"
"	border-radius: 5px; \n"
"	background-color: gray;\n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked\n"
"{ \n"
"	border: 1px solid #607cff; \n"
"	border-radius: 5px; \n"
"	background-color: #58fa53; \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 2px solid #6565"
                        "65;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #F0F0F0;\n"
"    gridline-color: #353635;\n"
"    outline : 0;\n"
"}\n"
"\n"
"QTableView::item:hover\n"
"{\n"
"    background-color: #24602b;\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"QTableView::item:selected\n"
"{\n"
"    background-color: #60c461;\n"
"    border: 2px solid #60c461;\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #505050;\n"
"    color: white;\n"
"}\n"
"\n"
"QHeaderView\n"
"{\n"
"    background-color: #505050;\n"
"    color: white;\n"
"    border-radius: 0px;\n"
"    text-align: left;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #505050;\n"
"    color: white;\n"
"    border-radius: 0px;\n"
"    text-align: left;\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #000000;\n"
"    background-color: #60c461;\n"
"}\n"
""
                        "\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"}\n"
"\n"
"\n"
"/*-----QTabWidget-----*/\n"
"QTabBar::tab\n"
"{\n"
"	background-color: #1f2b2b;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane\n"
"{\n"
"	background-color: transparent;\n"
"    border: 1px solid;\n"
"    border-color: #1f2b2b;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: #1f2b2b;\n"
""
                        "	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 0px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected:disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected \n"
"{\n"
"    background-color: #262626;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover \n"
"{\n"
"    background-color: #1f2b2b;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:!selected \n"
"{\n"
"    margin-top: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:bottom:!selected \n"
"{\n"
"    margin-bottom: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom \n"
"{\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:selected \n"
"{\n"
"    border-bottom-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:bottom:selected \n"
"{\n"
"    border-top-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:t"
                        "op:only-one, QTabBar::tab:bottom:only-one \n"
"{\n"
"    margin-right: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:!selected \n"
"{\n"
"    margin-right: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    margin-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right \n"
"{\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:selected \n"
"{\n"
"    border-left-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:right:selected \n"
"{\n"
"    border-right-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one \n"
"{\n"
"    margin-bottom: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
"QSlider \n"
"{\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"QSlider::groove:horizontal \n"
"{\n"
"	background-color: transparent;\n"
"	height: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal \n"
""
                        "{\n"
"	background-color: #41cd52;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal \n"
"{\n"
"	background-color: #a9a9aa;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"	background-color: #41cd52;\n"
"	width: 14px;\n"
"	margin-top: -6px;\n"
"	margin-bottom: -6px;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover \n"
"{\n"
"	background-color: #22af00;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled \n"
"{\n"
"	background-color: #bbb;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border: 1px solid #aaa;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::groove:vertical \n"
"{\n"
"	background-color: transparent;\n"
"	width: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:vertical \n"
"{\n"
"	background-color: #4"
                        "1cd52;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:vertical \n"
"{\n"
"	background-color: #a9a9aa;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical \n"
"{\n"
"	background-color: #41cd52;\n"
"	height: 14px;\n"
"	margin-left: -6px;\n"
"	margin-right: -6px;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical:hover \n"
"{\n"
"	background-color: #22af00;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:vertical:disabled \n"
"{\n"
"	background-color: #bbb;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:vertical:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border: 1px solid #aaa;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QDial-----*/\n"
"QDial\n"
"{\n"
"	background-color: #58ae53;\n"
"\n"
"}\n"
"\n"
"\n"
"QDial::disabled\n"
"{\n"
"	background-color: #404040;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrol"
                        "lBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #41cd52;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #41cd52;\n"
"    width: 14px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #41cd52;\n"
"    width: 14px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
""
                        "\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 13px;\n"
"    margin: 16px 0 16px 0;\n"
"    border: 1px solid #222222;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #41cd52;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #41cd52;\n"
"    height: 14px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border: 1px solid #41cd52;\n"
"    background-color: #41cd52;\n"
"    height: 14px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::do"
                        "wn-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar\n"
"{\n"
"	background-color: #a9a9aa;\n"
"	color: #000;\n"
"	border: 1px solid #000;\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: #36b9b1;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"	background-color: #656565;\n"
"	border: 1px solid #aaa;\n"
"	color: #656565;\n"
"}\n"
"\n"
"\n"
"QStatusBar\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0.100962 rgba(98, 197, 95, 255),stop:1 rgba(80, 158, 75, 255));\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}")
        self.choice_file = QAction(MainWindow)
        self.choice_file.setObjectName(u"choice_file")
        icon = QIcon()
        icon.addFile(u":/feather/file.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.choice_file.setIcon(icon)
        self.choice_dir = QAction(MainWindow)
        self.choice_dir.setObjectName(u"choice_dir")
        icon1 = QIcon()
        icon1.addFile(u":/feather/folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.choice_dir.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.lateral_menu = QWidget(self.centralwidget)
        self.lateral_menu.setObjectName(u"lateral_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lateral_menu.sizePolicy().hasHeightForWidth())
        self.lateral_menu.setSizePolicy(sizePolicy1)
        self.lateral_menu.setStyleSheet(u"QWidget {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.0113636, x2:0.96, y2:0.960227, stop:0 rgba(120, 19, 185, 100), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	background-color: #20afe7;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 11px;\n"
"	border-color: #2082ff;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #33bdff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 11px;\n"
"	border-color: #2082ff;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #2082ff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 11px;\n"
"	border-color: #2082ff;\n"
"	padding: 5px;\n"
"\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.lateral_menu)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icon_in_mmenu = QLabel(self.lateral_menu)
        self.icon_in_mmenu.setObjectName(u"icon_in_mmenu")
        sizePolicy1.setHeightForWidth(self.icon_in_mmenu.sizePolicy().hasHeightForWidth())
        self.icon_in_mmenu.setSizePolicy(sizePolicy1)
        self.icon_in_mmenu.setStyleSheet(u"background-color: none;")
        self.icon_in_mmenu.setPixmap(QPixmap(u":/feather/feather.svg"))

        self.horizontalLayout_2.addWidget(self.icon_in_mmenu)

        self.label = QLabel(self.lateral_menu)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: none;")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 500, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.group_recognition = QGroupBox(self.lateral_menu)
        self.group_recognition.setObjectName(u"group_recognition")
        self.group_recognition.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.group_recognition)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.but_rimage = QPushButton(self.group_recognition)
        self.but_rimage.setObjectName(u"but_rimage")
        icon2 = QIcon()
        icon2.addFile(u":/feather/camera.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_rimage.setIcon(icon2)
        self.but_rimage.setCheckable(True)

        self.verticalLayout_2.addWidget(self.but_rimage)

        self.but_rsound = QPushButton(self.group_recognition)
        self.but_rsound.setObjectName(u"but_rsound")
        icon3 = QIcon()
        icon3.addFile(u":/feather/activity.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_rsound.setIcon(icon3)
        self.but_rsound.setCheckable(True)

        self.verticalLayout_2.addWidget(self.but_rsound)

        self.but_pdf = QPushButton(self.group_recognition)
        self.but_pdf.setObjectName(u"but_pdf")
        icon4 = QIcon()
        icon4.addFile(u":/feather/book-open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_pdf.setIcon(icon4)
        self.but_pdf.setCheckable(True)

        self.verticalLayout_2.addWidget(self.but_pdf)


        self.verticalLayout_9.addLayout(self.verticalLayout_2)


        self.verticalLayout_10.addWidget(self.group_recognition)

        self.frame_3 = QFrame(self.lateral_menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"#frame_3  {\n"
"background-color: none;\n"
"}\n"
"\n"
"#frame_2 {	\n"
"background-color: rgba(0, 0, 0, 20);\n"
"border-radius: 5px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.but_information = QPushButton(self.frame_3)
        self.but_information.setObjectName(u"but_information")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(10)
        self.but_information.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/feather/align-justify.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_information.setIcon(icon5)
        self.but_information.setCheckable(True)
        self.but_information.setChecked(False)

        self.verticalLayout_4.addWidget(self.but_information)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.but_guide = QPushButton(self.frame_2)
        self.but_guide.setObjectName(u"but_guide")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(8)
        font2.setBold(True)
        self.but_guide.setFont(font2)
        icon6 = QIcon()
        icon6.addFile(u":/feather/help-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_guide.setIcon(icon6)
        self.but_guide.setCheckable(True)

        self.verticalLayout_3.addWidget(self.but_guide)

        self.but_developer = QPushButton(self.frame_2)
        self.but_developer.setObjectName(u"but_developer")
        self.but_developer.setFont(font2)
        self.but_developer.setCheckable(True)

        self.verticalLayout_3.addWidget(self.but_developer)

        self.but_technologies = QPushButton(self.frame_2)
        self.but_technologies.setObjectName(u"but_technologies")
        self.but_technologies.setFont(font2)
        self.but_technologies.setCheckable(True)

        self.verticalLayout_3.addWidget(self.but_technologies)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.pushButton = QPushButton(self.lateral_menu)
        self.pushButton.setObjectName(u"pushButton")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.pushButton.setFont(font3)
        self.pushButton.setLayoutDirection(Qt.RightToLeft)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #ff4d4d;  /* \u041a\u0440\u0430\u0441\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 */\n"
"    padding: 10px 20px;         /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u0441\u0442\u0440\u043e\u0435\u043d\u043d\u044b\u0445 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 */\n"
"    border: none;               /* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u0440\u0430\u043c\u043a\u0443 */\n"
"    border-radius: 10px;        /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    transition: background-color 0.3s, transform 0.2s;  /* \u041f\u043b\u0430\u0432\u043d\u044b\u0439 \u043f\u0435\u0440\u0435\u0445\u043e\u0434 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e60000;  /* \u0422\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	transition: background-color 1s;\n"
"	background-color: rgb(138"
                        ", 21, 10);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/feather/arrow-right-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(18, 18))

        self.verticalLayout_10.addWidget(self.pushButton)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 5)
        self.verticalLayout_10.setStretch(2, 5)
        self.verticalLayout_10.setStretch(3, 5)

        self.horizontalLayout.addWidget(self.lateral_menu)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_widget = QWidget(self.centralwidget)
        self.title_widget.setObjectName(u"title_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.title_widget.sizePolicy().hasHeightForWidth())
        self.title_widget.setSizePolicy(sizePolicy2)
        self.title_widget.setAcceptDrops(False)
        self.horizontalLayout_3 = QHBoxLayout(self.title_widget)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_title = QLabel(self.title_widget)
        self.label_title.setObjectName(u"label_title")
        font4 = QFont()
        font4.setFamilies([u"ScriptS"])
        font4.setPointSize(30)
        font4.setBold(False)
        font4.setItalic(True)
        self.label_title.setFont(font4)
        self.label_title.setStyleSheet(u"border-radius: 50px;")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_title)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 10)
        self.settings_process = QComboBox(self.title_widget)
        icon8 = QIcon()
        icon8.addFile(u":/feather/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_process.addItem(icon8, "")
        self.settings_process.addItem(icon8, "")
        self.settings_process.addItem(icon8, "")
        self.settings_process.setObjectName(u"settings_process")
        self.settings_process.setIconSize(QSize(12, 12))

        self.verticalLayout_6.addWidget(self.settings_process)

        self.but_edit = QPushButton(self.title_widget)
        self.but_edit.setObjectName(u"but_edit")

        self.verticalLayout_6.addWidget(self.but_edit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.horizontalLayout_3.setStretch(0, 8)

        self.verticalLayout.addWidget(self.title_widget)

        self.work_widget = QWidget(self.centralwidget)
        self.work_widget.setObjectName(u"work_widget")
        sizePolicy1.setHeightForWidth(self.work_widget.sizePolicy().hasHeightForWidth())
        self.work_widget.setSizePolicy(sizePolicy1)
        self.work_widget.setStyleSheet(u"#work_widget {	\n"
"background-color: rgba(25, 3, 152, 20);\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.work_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stackedWidget = QStackedWidget(self.work_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setFocusPolicy(Qt.NoFocus)
        self.stackedWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.stackedWidget.setStyleSheet(u"#page_image, #page_sound, #page_guide, #page_developer, #page_technologies, #page_pdf {\n"
"background-color: rgba(25, 3, 152, 20);\n"
"}\n"
"\n"
"QRadioButton {\n"
"    spacing: 5px;\n"
"	font-size: 16px;\n"
"	color: rgb(0, 0, 0);\n"
" }\n"
"   QRadioButton::indicator {\n"
"    width: 14px;\n"
"     height: 14px;\n"
"}\n"
"QRadioButton::indicator:unchecked {\n"
"    border: 2px solid #007BFF;\n"
"     background: white;\n"
" }\n"
"QRadioButton::indicator:checked {\n"
"    border: 2px solid #0056b3;\n"
"    background: #007BFF;\n"
"}\n"
"\n"
"")
        self.stackedWidget.setInputMethodHints(Qt.ImhNone)
        self.page_image = QWidget()
        self.page_image.setObjectName(u"page_image")
        self.page_image.setContextMenuPolicy(Qt.NoContextMenu)
        self.horizontalLayout_5 = QHBoxLayout(self.page_image)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_image = QLabel(self.page_image)
        self.label_image.setObjectName(u"label_image")
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(20)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setKerning(True)
        self.label_image.setFont(font5)
        self.label_image.setStyleSheet(u"")
        self.label_image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_image)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.page_image)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setFamilies([u"Times New Roman"])
        font6.setPointSize(16)
        self.label_2.setFont(font6)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.text_edit_image = QTextEdit(self.page_image)
        self.text_edit_image.setObjectName(u"text_edit_image")
        self.text_edit_image.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.text_edit_image)

        self.but_recognition_image = QPushButton(self.page_image)
        self.but_recognition_image.setObjectName(u"but_recognition_image")
        font7 = QFont()
        font7.setFamilies([u"Times New Roman"])
        font7.setPointSize(15)
        font7.setUnderline(True)
        self.but_recognition_image.setFont(font7)
        icon9 = QIcon()
        icon9.addFile(u":/feather/aperture.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_recognition_image.setIcon(icon9)
        self.but_recognition_image.setIconSize(QSize(18, 18))

        self.verticalLayout_8.addWidget(self.but_recognition_image)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 4)
        self.stackedWidget.addWidget(self.page_image)
        self.page_sound = QWidget()
        self.page_sound.setObjectName(u"page_sound")
        self.horizontalLayout_6 = QHBoxLayout(self.page_sound)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_select_audio_file = QLabel(self.page_sound)
        self.label_select_audio_file.setObjectName(u"label_select_audio_file")
        font8 = QFont()
        font8.setFamilies([u"Times New Roman"])
        font8.setPointSize(22)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setUnderline(False)
        self.label_select_audio_file.setFont(font8)
        self.label_select_audio_file.setLayoutDirection(Qt.LeftToRight)
        self.label_select_audio_file.setStyleSheet(u"QLabel {\n"
"            transform: rotate(90deg); /* \u041f\u043e\u0432\u043e\u0440\u0430\u0447\u0438\u0432\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u043d\u0430 90 \u0433\u0440\u0430\u0434\u0443\u0441\u043e\u0432 */\n"
"            transform-origin: left bottom; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0442\u043e\u0447\u043a\u0443 \u043f\u043e\u0432\u043e\u0440\u043e\u0442\u0430 */\n"
"}")
        self.label_select_audio_file.setScaledContents(False)
        self.label_select_audio_file.setAlignment(Qt.AlignCenter)
        self.label_select_audio_file.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_select_audio_file)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.page_sound)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font6)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_3)

        self.text_edit_sound = QTextEdit(self.page_sound)
        self.text_edit_sound.setObjectName(u"text_edit_sound")
        self.text_edit_sound.setReadOnly(True)

        self.verticalLayout_12.addWidget(self.text_edit_sound)

        self.but_recognition_sound = QPushButton(self.page_sound)
        self.but_recognition_sound.setObjectName(u"but_recognition_sound")
        self.but_recognition_sound.setFont(font7)
        self.but_recognition_sound.setIcon(icon9)
        self.but_recognition_sound.setIconSize(QSize(18, 18))

        self.verticalLayout_12.addWidget(self.but_recognition_sound)


        self.horizontalLayout_6.addLayout(self.verticalLayout_12)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 7)
        self.stackedWidget.addWidget(self.page_sound)
        self.page_pdf = QWidget()
        self.page_pdf.setObjectName(u"page_pdf")
        self.horizontalLayout_7 = QHBoxLayout(self.page_pdf)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_select_pdf_file = QLabel(self.page_pdf)
        self.label_select_pdf_file.setObjectName(u"label_select_pdf_file")
        self.label_select_pdf_file.setFont(font8)
        self.label_select_pdf_file.setLayoutDirection(Qt.LeftToRight)
        self.label_select_pdf_file.setStyleSheet(u"QLabel {\n"
"            transform: rotate(90deg); /* \u041f\u043e\u0432\u043e\u0440\u0430\u0447\u0438\u0432\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u043d\u0430 90 \u0433\u0440\u0430\u0434\u0443\u0441\u043e\u0432 */\n"
"            transform-origin: left bottom; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0442\u043e\u0447\u043a\u0443 \u043f\u043e\u0432\u043e\u0440\u043e\u0442\u0430 */\n"
"}")
        self.label_select_pdf_file.setScaledContents(False)
        self.label_select_pdf_file.setAlignment(Qt.AlignCenter)
        self.label_select_pdf_file.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.label_select_pdf_file)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_4 = QLabel(self.page_pdf)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font6)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_4)

        self.text_edit_pdf = QTextEdit(self.page_pdf)
        self.text_edit_pdf.setObjectName(u"text_edit_pdf")
        self.text_edit_pdf.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.text_edit_pdf)

        self.but_recognition_pdf = QPushButton(self.page_pdf)
        self.but_recognition_pdf.setObjectName(u"but_recognition_pdf")
        self.but_recognition_pdf.setFont(font7)
        self.but_recognition_pdf.setIcon(icon9)
        self.but_recognition_pdf.setIconSize(QSize(18, 18))

        self.verticalLayout_13.addWidget(self.but_recognition_pdf)


        self.horizontalLayout_7.addLayout(self.verticalLayout_13)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 7)
        self.stackedWidget.addWidget(self.page_pdf)
        self.page_guide = QWidget()
        self.page_guide.setObjectName(u"page_guide")
        self.verticalLayout_14 = QVBoxLayout(self.page_guide)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_guide = QLabel(self.page_guide)
        self.label_guide.setObjectName(u"label_guide")
        self.label_guide.setFont(font6)
        self.label_guide.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_guide)

        self.plainTextEdit_guide = QPlainTextEdit(self.page_guide)
        self.plainTextEdit_guide.setObjectName(u"plainTextEdit_guide")
        font9 = QFont()
        font9.setPointSize(14)
        self.plainTextEdit_guide.setFont(font9)
        self.plainTextEdit_guide.setReadOnly(True)

        self.verticalLayout_14.addWidget(self.plainTextEdit_guide)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radbut_ru1 = QRadioButton(self.page_guide)
        self.radbut_ru1.setObjectName(u"radbut_ru1")
        font10 = QFont()
        self.radbut_ru1.setFont(font10)

        self.horizontalLayout_8.addWidget(self.radbut_ru1)

        self.radbut_en1 = QRadioButton(self.page_guide)
        self.radbut_en1.setObjectName(u"radbut_en1")
        self.radbut_en1.setFont(font10)
        self.radbut_en1.setChecked(True)

        self.horizontalLayout_8.addWidget(self.radbut_en1)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)

        self.stackedWidget.addWidget(self.page_guide)
        self.page_developer = QWidget()
        self.page_developer.setObjectName(u"page_developer")
        self.verticalLayout_15 = QVBoxLayout(self.page_developer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_github_icon = QLabel(self.page_developer)
        self.label_github_icon.setObjectName(u"label_github_icon")
        self.label_github_icon.setStyleSheet(u"background-color: rgb(228, 255, 234);\n"
"border-radius: 5px;")
        self.label_github_icon.setPixmap(QPixmap(u":/feather/github.svg"))

        self.horizontalLayout_9.addWidget(self.label_github_icon)

        self.label_my_github = QLabel(self.page_developer)
        self.label_my_github.setObjectName(u"label_my_github")
        self.label_my_github.setStyleSheet(u"background-color: rgba(162, 255, 189, 60);")
        self.label_my_github.setOpenExternalLinks(False)

        self.horizontalLayout_9.addWidget(self.label_my_github)

        self.label_developer = QLabel(self.page_developer)
        self.label_developer.setObjectName(u"label_developer")
        self.label_developer.setFont(font6)
        self.label_developer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_developer)

        self.horizontalLayout_9.setStretch(2, 3)

        self.verticalLayout_15.addLayout(self.horizontalLayout_9)

        self.plainTextEdit_developer = QPlainTextEdit(self.page_developer)
        self.plainTextEdit_developer.setObjectName(u"plainTextEdit_developer")
        self.plainTextEdit_developer.setFont(font9)
        self.plainTextEdit_developer.setReadOnly(True)

        self.verticalLayout_15.addWidget(self.plainTextEdit_developer)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.radbut_ru2 = QRadioButton(self.page_developer)
        self.radbut_ru2.setObjectName(u"radbut_ru2")
        self.radbut_ru2.setFont(font10)

        self.horizontalLayout_10.addWidget(self.radbut_ru2)

        self.radbut_en2 = QRadioButton(self.page_developer)
        self.radbut_en2.setObjectName(u"radbut_en2")
        self.radbut_en2.setFont(font10)
        self.radbut_en2.setChecked(True)

        self.horizontalLayout_10.addWidget(self.radbut_en2)


        self.verticalLayout_15.addLayout(self.horizontalLayout_10)

        self.stackedWidget.addWidget(self.page_developer)
        self.page_technologies = QWidget()
        self.page_technologies.setObjectName(u"page_technologies")
        self.verticalLayout_16 = QVBoxLayout(self.page_technologies)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_technologies = QLabel(self.page_technologies)
        self.label_technologies.setObjectName(u"label_technologies")
        self.label_technologies.setFont(font6)
        self.label_technologies.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_technologies)

        self.plainTextEdit_technologies = QPlainTextEdit(self.page_technologies)
        self.plainTextEdit_technologies.setObjectName(u"plainTextEdit_technologies")
        self.plainTextEdit_technologies.setFont(font9)
        self.plainTextEdit_technologies.setReadOnly(True)

        self.verticalLayout_16.addWidget(self.plainTextEdit_technologies)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.radbut_ru3 = QRadioButton(self.page_technologies)
        self.radbut_ru3.setObjectName(u"radbut_ru3")
        self.radbut_ru3.setFont(font10)

        self.horizontalLayout_11.addWidget(self.radbut_ru3)

        self.radbut_en3 = QRadioButton(self.page_technologies)
        self.radbut_en3.setObjectName(u"radbut_en3")
        self.radbut_en3.setFont(font10)
        self.radbut_en3.setChecked(True)

        self.horizontalLayout_11.addWidget(self.radbut_en3)


        self.verticalLayout_16.addLayout(self.horizontalLayout_11)

        self.stackedWidget.addWidget(self.page_technologies)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.work_widget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_res = QLabel(self.centralwidget)
        self.icon_res.setObjectName(u"icon_res")
        self.icon_res.setStyleSheet(u"background-color: rgba(171, 184, 255, 100);\n"
"padding-right: 10px;")
        self.icon_res.setPixmap(QPixmap(u":/feather/alert-octagon.svg"))

        self.horizontalLayout_4.addWidget(self.icon_res)

        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.result.sizePolicy().hasHeightForWidth())
        self.result.setSizePolicy(sizePolicy4)
        self.result.setMinimumSize(QSize(0, 0))
        self.result.setMaximumSize(QSize(16777215, 1000))
        font11 = QFont()
        font11.setFamilies([u"Times New Roman"])
        font11.setPointSize(12)
        self.result.setFont(font11)
        self.result.setStyleSheet(u"background-color: rgba(171, 184, 255, 100);\n"
"color: rgb(2, 2, 2);")

        self.horizontalLayout_4.addWidget(self.result)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 2)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(1, 11)

        self.verticalLayout_11.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1125, 21))
        self.top_menu = QMenu(self.menubar)
        self.top_menu.setObjectName(u"top_menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.top_menu.menuAction())
        self.top_menu.addAction(self.choice_file)
        self.top_menu.addAction(self.choice_dir)

        self.retranslateUi(MainWindow)
        self.but_information.toggled.connect(self.frame_2.setHidden)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.choice_file.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.choice_dir.setText(QCoreApplication.translate("MainWindow", u"Directory", None))
        self.icon_in_mmenu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Choose", None))
        self.group_recognition.setTitle(QCoreApplication.translate("MainWindow", u"Recognition", None))
        self.but_rimage.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.but_rsound.setText(QCoreApplication.translate("MainWindow", u"Sound", None))
        self.but_pdf.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.but_information.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.but_guide.setText(QCoreApplication.translate("MainWindow", u"Guide", None))
        self.but_developer.setText(QCoreApplication.translate("MainWindow", u"Developer", None))
        self.but_technologies.setText(QCoreApplication.translate("MainWindow", u"Technologies", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" EXIT", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"toText", None))
        self.settings_process.setItemText(0, QCoreApplication.translate("MainWindow", u"Settings from image", None))
        self.settings_process.setItemText(1, QCoreApplication.translate("MainWindow", u"Settingd from sound", None))
        self.settings_process.setItemText(2, QCoreApplication.translate("MainWindow", u"Settings from PDF", None))

        self.but_edit.setText(QCoreApplication.translate("MainWindow", u"edit", None))
        self.label_image.setText(QCoreApplication.translate("MainWindow", u"Select the image above", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Recognized text ", None))
        self.text_edit_image.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.but_recognition_image.setText(QCoreApplication.translate("MainWindow", u"Recognized", None))
        self.label_select_audio_file.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Select the audio file above</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Recognized text ", None))
        self.but_recognition_sound.setText(QCoreApplication.translate("MainWindow", u"Recognized", None))
        self.label_select_pdf_file.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Select the PDF file above</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Recognized text ", None))
        self.but_recognition_pdf.setText(QCoreApplication.translate("MainWindow", u"Recognized", None))
        self.label_guide.setText(QCoreApplication.translate("MainWindow", u"Guide", None))
        self.plainTextEdit_guide.setPlainText("")
        self.radbut_ru1.setText(QCoreApplication.translate("MainWindow", u"ru", None))
        self.radbut_en1.setText(QCoreApplication.translate("MainWindow", u"en", None))
        self.label_github_icon.setText("")
        self.label_my_github.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/IvanGaideek/\"><span style=\" text-decoration: underline; color:#0000ff;\">My GitHub</span></a></p></body></html>", None))
        self.label_developer.setText(QCoreApplication.translate("MainWindow", u"Developer", None))
        self.plainTextEdit_developer.setPlainText("")
        self.radbut_ru2.setText(QCoreApplication.translate("MainWindow", u"ru", None))
        self.radbut_en2.setText(QCoreApplication.translate("MainWindow", u"en", None))
        self.label_technologies.setText(QCoreApplication.translate("MainWindow", u"Technologies", None))
        self.plainTextEdit_technologies.setPlainText("")
        self.radbut_ru3.setText(QCoreApplication.translate("MainWindow", u"ru", None))
        self.radbut_en3.setText(QCoreApplication.translate("MainWindow", u"en", None))
        self.icon_res.setText("")
        self.result.setText(QCoreApplication.translate("MainWindow", u"Here is the analysis of the result", None))
        self.top_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

