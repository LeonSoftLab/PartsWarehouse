# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_EditPart.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_EditPartForm(object):
    def setupUi(self, EditPartForm):
        if not EditPartForm.objectName():
            EditPartForm.setObjectName(u"EditPartForm")
        EditPartForm.resize(536, 472)
        self.verticalLayout_2 = QVBoxLayout(EditPartForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame1 = QFrame(EditPartForm)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;")
        self.horizontalLayout = QHBoxLayout(self.frame1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_cat = QLabel(self.frame1)
        self.label_cat.setObjectName(u"label_cat")
        self.label_cat.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout.addWidget(self.label_cat)

        self.cmb_cat = QComboBox(self.frame1)
        self.cmb_cat.setObjectName(u"cmb_cat")
        self.cmb_cat.setStyleSheet(u"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"margin: 2px;\n"
"padding: 3px;")

        self.horizontalLayout.addWidget(self.cmb_cat)

        self.btn_edit_cat = QPushButton(self.frame1)
        self.btn_edit_cat.setObjectName(u"btn_edit_cat")
        self.btn_edit_cat.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(207, 0, 3, 100);\n"
"font: 10pt \"Arial\";\n"
"margin: 5px;\n"
"padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(2, 144, 0, 100);\n"
"color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(2, 144, 0, 150);\n"
"color:white;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_edit_cat)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.frame1)

        self.frame2 = QFrame(EditPartForm)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setStyleSheet(u"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;")
        self.horizontalLayout_2 = QHBoxLayout(self.frame2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_vendor = QLabel(self.frame2)
        self.label_vendor.setObjectName(u"label_vendor")
        self.label_vendor.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_vendor)

        self.cmb_vendor = QComboBox(self.frame2)
        self.cmb_vendor.setObjectName(u"cmb_vendor")
        self.cmb_vendor.setStyleSheet(u"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"margin: 2px;\n"
"padding: 3px;")

        self.horizontalLayout_2.addWidget(self.cmb_vendor)

        self.btn_edit_vendor = QPushButton(self.frame2)
        self.btn_edit_vendor.setObjectName(u"btn_edit_vendor")
        self.btn_edit_vendor.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(207, 0, 3, 100);\n"
"font: 10pt \"Arial\";\n"
"margin: 5px;\n"
"padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(2, 144, 0, 100);\n"
"color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(2, 144, 0, 150);\n"
"color:white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_edit_vendor)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.frame2)

        self.frame3 = QFrame(EditPartForm)
        self.frame3.setObjectName(u"frame3")
        self.frame3.setStyleSheet(u"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;")
        self.horizontalLayout_3 = QHBoxLayout(self.frame3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_name = QLabel(self.frame3)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.frame3)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setStyleSheet(u"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 14pt;\n"
"margin: 2px;\n"
"padding: 3px;")

        self.horizontalLayout_3.addWidget(self.lineEdit_name)


        self.verticalLayout_2.addWidget(self.frame3)

        self.frame4 = QFrame(EditPartForm)
        self.frame4.setObjectName(u"frame4")
        self.frame4.setStyleSheet(u"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;")
        self.verticalLayout = QVBoxLayout(self.frame4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_notes = QLabel(self.frame4)
        self.label_notes.setObjectName(u"label_notes")
        self.label_notes.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_notes)

        self.textEdit_notes = QTextEdit(self.frame4)
        self.textEdit_notes.setObjectName(u"textEdit_notes")
        self.textEdit_notes.setStyleSheet(u"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 14pt;\n"
"margin: 2px;\n"
"padding: 3px;")

        self.verticalLayout.addWidget(self.textEdit_notes)


        self.verticalLayout_2.addWidget(self.frame4)

        self.btn_save = QPushButton(EditPartForm)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"font: 12pt \"Arial\";\n"
"margin: 5px;\n"
"padding: 5px;\n"
"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(2, 144, 0, 100);\n"
"color:white;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(2, 144, 0, 150);\n"
"color:white;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_save)


        self.retranslateUi(EditPartForm)

        QMetaObject.connectSlotsByName(EditPartForm)
    # setupUi

    def retranslateUi(self, EditPartForm):
        EditPartForm.setWindowTitle(QCoreApplication.translate("EditPartForm", u"Dialog", None))
        self.label_cat.setText(QCoreApplication.translate("EditPartForm", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.btn_edit_cat.setText(QCoreApplication.translate("EditPartForm", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_vendor.setText(QCoreApplication.translate("EditPartForm", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None))
        self.btn_edit_vendor.setText(QCoreApplication.translate("EditPartForm", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_name.setText(QCoreApplication.translate("EditPartForm", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_notes.setText(QCoreApplication.translate("EditPartForm", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.btn_save.setText(QCoreApplication.translate("EditPartForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

