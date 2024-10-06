# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_for_image_des.ui'
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
    QDialogButtonBox, QDoubleSpinBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_SettingsImage(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(576, 383)
        Form.setMinimumSize(QSize(576, 383))
        Form.setMaximumSize(QSize(650, 450))
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
        self.verticalLayout_11 = QVBoxLayout(Form)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(238, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.check_to_txt = QCheckBox(self.frame_3)
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

        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.lineEdit_folder_path = QLineEdit(self.frame_3)
        self.lineEdit_folder_path.setObjectName(u"lineEdit_folder_path")

        self.horizontalLayout_5.addWidget(self.lineEdit_folder_path)

        self.choose_folder_save_but = QPushButton(self.frame_3)
        self.choose_folder_save_but.setObjectName(u"choose_folder_save_but")

        self.horizontalLayout_5.addWidget(self.choose_folder_save_but)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_9.addWidget(self.frame_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.input_langs = QLineEdit(Form)
        self.input_langs.setObjectName(u"input_langs")

        self.horizontalLayout_7.addWidget(self.input_langs)

        self.comboBox_langs = QComboBox(Form)
        self.comboBox_langs.setObjectName(u"comboBox_langs")

        self.horizontalLayout_7.addWidget(self.comboBox_langs)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.error_input = QLabel(Form)
        self.error_input.setObjectName(u"error_input")
        self.error_input.setStyleSheet(u"color: rgb(235, 0, 3);")

        self.verticalLayout_8.addWidget(self.error_input)

        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 3)
        self.verticalLayout_8.setStretch(2, 1)

        self.verticalLayout_9.addLayout(self.verticalLayout_8)

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

        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.verticalLayout_9.setStretch(0, 2)
        self.verticalLayout_9.setStretch(1, 2)
        self.verticalLayout_9.setStretch(2, 1)

        self.horizontalLayout_9.addLayout(self.verticalLayout_9)

        self.advance_set_image_group = QGroupBox(Form)
        self.advance_set_image_group.setObjectName(u"advance_set_image_group")
        self.advance_set_image_group.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.advance_set_image_group)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.advance_set_image_group)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.prerrocessing_image_but = QPushButton(self.frame_2)
        self.prerrocessing_image_but.setObjectName(u"prerrocessing_image_but")
        self.prerrocessing_image_but.setCheckable(True)
        self.prerrocessing_image_but.setChecked(False)
        self.prerrocessing_image_but.setAutoRepeat(False)

        self.verticalLayout_4.addWidget(self.prerrocessing_image_but)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.size_SpinBox = QDoubleSpinBox(self.frame)
        self.size_SpinBox.setObjectName(u"size_SpinBox")
        self.size_SpinBox.setMinimum(0.500000000000000)
        self.size_SpinBox.setMaximum(8.000000000000000)
        self.size_SpinBox.setSingleStep(0.500000000000000)
        self.size_SpinBox.setValue(1.500000000000000)

        self.horizontalLayout.addWidget(self.size_SpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.check_gray = QCheckBox(self.frame)
        self.check_gray.setObjectName(u"check_gray")
        self.check_gray.setChecked(True)

        self.horizontalLayout_2.addWidget(self.check_gray)

        self.check_bitmap = QCheckBox(self.frame)
        self.check_bitmap.setObjectName(u"check_bitmap")
        self.check_bitmap.setChecked(True)

        self.horizontalLayout_2.addWidget(self.check_bitmap)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.contract_SpinBox = QDoubleSpinBox(self.frame)
        self.contract_SpinBox.setObjectName(u"contract_SpinBox")
        self.contract_SpinBox.setMinimum(0.400000000000000)
        self.contract_SpinBox.setMaximum(3.000000000000000)
        self.contract_SpinBox.setSingleStep(0.050000000000000)
        self.contract_SpinBox.setValue(1.750000000000000)

        self.horizontalLayout_3.addWidget(self.contract_SpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.check_invert = QCheckBox(self.frame)
        self.check_invert.setObjectName(u"check_invert")
        self.check_invert.setChecked(True)

        self.verticalLayout_2.addWidget(self.check_invert)


        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.advance_set_image_group)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_image_before = QLabel(self.advance_set_image_group)
        self.label_image_before.setObjectName(u"label_image_before")

        self.verticalLayout_6.addWidget(self.label_image_before)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 4)

        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.label_4 = QLabel(self.advance_set_image_group)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"margin: auto, auto;\n"
"")
        self.label_4.setPixmap(QPixmap(u":/feather/arrow-right.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.advance_set_image_group)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_image_after = QLabel(self.advance_set_image_group)
        self.label_image_after.setObjectName(u"label_image_after")

        self.verticalLayout_5.addWidget(self.label_image_after)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 4)

        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_9.addWidget(self.advance_set_image_group)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_3 = QSpacerItem(398, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.accepting_response = QDialogButtonBox(Form)
        self.accepting_response.setObjectName(u"accepting_response")
        self.accepting_response.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_10.addWidget(self.accepting_response)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)


        self.retranslateUi(Form)
        self.prerrocessing_image_but.toggled.connect(self.frame.setHidden)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Image Settings", None))
        self.check_to_txt.setText(QCoreApplication.translate("Form", u"Save to .txt files", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"The folder to save", None))
        self.lineEdit_folder_path.setPlaceholderText(QCoreApplication.translate("Form", u"Path ...", None))
        self.choose_folder_save_but.setText(QCoreApplication.translate("Form", u"Choose", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0421hoose languages", None))
        self.input_langs.setPlaceholderText(QCoreApplication.translate("Form", u"lang1, lang2 ...", None))
        self.error_input.setText("")
        self.turn_off_settings.setText(QCoreApplication.translate("Form", u"turn off", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Default settings", None))
        self.advance_set_image_group.setTitle(QCoreApplication.translate("Form", u"Advanced Settings", None))
        self.prerrocessing_image_but.setText(QCoreApplication.translate("Form", u"Image Preprocessing", None))
        self.label.setText(QCoreApplication.translate("Form", u"Size transform:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Convert", None))
        self.check_gray.setText(QCoreApplication.translate("Form", u"to Gray", None))
        self.check_bitmap.setText(QCoreApplication.translate("Form", u"to Bitmap", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Contrast ratio", None))
        self.check_invert.setText(QCoreApplication.translate("Form", u"invert", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Before", None))
        self.label_image_before.setText("")
        self.label_4.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"After", None))
        self.label_image_after.setText("")
    # retranslateUi

