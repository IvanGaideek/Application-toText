# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_for_sound_des.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import icons_rc
import icons_rc

class Ui_SettingsSound(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(450, 320)
        Form.setMinimumSize(QSize(400, 300))
        Form.setMaximumSize(QSize(450, 320))
        Form.setStyleSheet(u"#Form {\n"
"	background-color: rgb(0, 217, 68);\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDoubleSpinBox, #label_image_before, #label_image_after {\n"
"	border-radius: 2px;\n"
"	background-color: rgb(26, 244, 255, 88);\n"
"}\n"
"\n"
"#label_image_before, #label_image_after {\n"
"	border-radius: 5px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(238, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.check_to_txt = QCheckBox(Form)
        self.check_to_txt.setObjectName(u"check_to_txt")
        font = QFont()
        font.setPointSize(10)
        self.check_to_txt.setFont(font)
        self.check_to_txt.setLayoutDirection(Qt.LeftToRight)
        self.check_to_txt.setAutoFillBackground(False)
        self.check_to_txt.setInputMethodHints(Qt.ImhNone)
        self.check_to_txt.setTristate(False)

        self.horizontalLayout_6.addWidget(self.check_to_txt)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.lineEdit_folder_path = QLineEdit(Form)
        self.lineEdit_folder_path.setObjectName(u"lineEdit_folder_path")

        self.horizontalLayout_5.addWidget(self.lineEdit_folder_path)

        self.choose_folder_save_but = QPushButton(Form)
        self.choose_folder_save_but.setObjectName(u"choose_folder_save_but")

        self.horizontalLayout_5.addWidget(self.choose_folder_save_but)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_10)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox_langs = QComboBox(Form)
        self.comboBox_langs.setObjectName(u"comboBox_langs")

        self.verticalLayout.addWidget(self.comboBox_langs)

        self.comboBox_models = QComboBox(Form)
        self.comboBox_models.setObjectName(u"comboBox_models")

        self.verticalLayout.addWidget(self.comboBox_models)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.turn_off_settings = QPushButton(Form)
        self.turn_off_settings.setObjectName(u"turn_off_settings")

        self.horizontalLayout_8.addWidget(self.turn_off_settings)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 8)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)

        self.accepting_response = QDialogButtonBox(Form)
        self.accepting_response.setObjectName(u"accepting_response")
        self.accepting_response.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_2.addWidget(self.accepting_response)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Sound Settings", None))
        self.check_to_txt.setText(QCoreApplication.translate("Form", u"Save to .txt files", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"The folder to save", None))
        self.lineEdit_folder_path.setPlaceholderText(QCoreApplication.translate("Form", u"Path ...", None))
        self.choose_folder_save_but.setText(QCoreApplication.translate("Form", u"Choose", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0421hoose language:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u0421hoose model:", None))
        self.turn_off_settings.setText(QCoreApplication.translate("Form", u"turn off", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Default settings", None))
    # retranslateUi

