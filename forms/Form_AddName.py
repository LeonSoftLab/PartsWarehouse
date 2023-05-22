# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_AddName.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddNameForm(object):
    def setupUi(self, AddNameForm):
        if not AddNameForm.objectName():
            AddNameForm.setObjectName(u"AddNameForm")
        AddNameForm.resize(450, 319)
        self.verticalLayout_2 = QVBoxLayout(AddNameForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame2 = QFrame(AddNameForm)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setStyleSheet(u"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;")
        self.verticalLayout = QVBoxLayout(self.frame2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(self.frame2)
        self.label_name.setObjectName(u"label_name")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_name)

        self.edit_name = QLineEdit(self.frame2)
        self.edit_name.setObjectName(u"edit_name")
        self.edit_name.setStyleSheet(u"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 14pt;\n"
"margin: 2px;\n"
"padding: 3px;")

        self.verticalLayout.addWidget(self.edit_name)


        self.verticalLayout_2.addWidget(self.frame2)

        self.edit_note = QPlainTextEdit(AddNameForm)
        self.edit_note.setObjectName(u"edit_note")
        self.edit_note.setStyleSheet(u"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 14pt;\n"
"margin: 2px;\n"
"padding: 3px;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;")

        self.verticalLayout_2.addWidget(self.edit_note)

        self.frame1 = QFrame(AddNameForm)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;")
        self.horizontalLayout = QHBoxLayout(self.frame1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_ok = QPushButton(self.frame1)
        self.btn_ok.setObjectName(u"btn_ok")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.btn_ok.setFont(font1)
        self.btn_ok.setStyleSheet(u"QPushButton {\n"
"font: 12pt \"Arial\";\n"
"margin: 5px;\n"
"padding: 5px;\n"
"color: black;\n"
"font-weight: bold;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(2, 144, 0, 100);\n"
"color:white;\n"
"font-weight: bold;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(2, 144, 0, 150);\n"
"color:white;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_ok)

        self.btn_cancel = QPushButton(self.frame1)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setStyleSheet(u"QPushButton {\n"
"font: 12pt \"Arial\";\n"
"margin: 5px;\n"
"padding: 5px;\n"
"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(207, 0, 3, 100);\n"
"color:white;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(207, 0, 3, 150);\n"
"color:white;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout_2.addWidget(self.frame1)


        self.retranslateUi(AddNameForm)

        QMetaObject.connectSlotsByName(AddNameForm)
    # setupUi

    def retranslateUi(self, AddNameForm):
        AddNameForm.setWindowTitle(QCoreApplication.translate("AddNameForm", u"Dialog", None))
        self.label_name.setText(QCoreApplication.translate("AddNameForm", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.btn_ok.setText(QCoreApplication.translate("AddNameForm", u"\u041e\u043a", None))
        self.btn_cancel.setText(QCoreApplication.translate("AddNameForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

