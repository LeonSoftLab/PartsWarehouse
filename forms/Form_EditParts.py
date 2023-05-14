# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_EditParts.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_EditPartsForm(object):
    def setupUi(self, EditPartsForm):
        if not EditPartsForm.objectName():
            EditPartsForm.setObjectName(u"EditPartsForm")
        EditPartsForm.resize(457, 299)
        self.label_type = QLabel(EditPartsForm)
        self.label_type.setObjectName(u"label_type")
        self.label_type.setGeometry(QRect(20, 20, 49, 16))
        self.comboBox_type = QComboBox(EditPartsForm)
        self.comboBox_type.setObjectName(u"comboBox_type")
        self.comboBox_type.setGeometry(QRect(110, 20, 211, 22))
        self.label_vendor = QLabel(EditPartsForm)
        self.label_vendor.setObjectName(u"label_vendor")
        self.label_vendor.setGeometry(QRect(20, 50, 81, 16))
        self.comboBox_vendor = QComboBox(EditPartsForm)
        self.comboBox_vendor.setObjectName(u"comboBox_vendor")
        self.comboBox_vendor.setGeometry(QRect(110, 50, 211, 22))
        self.label_name = QLabel(EditPartsForm)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(20, 80, 91, 21))
        self.lineEdit_name = QLineEdit(EditPartsForm)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(110, 80, 321, 22))
        self.label_notes = QLabel(EditPartsForm)
        self.label_notes.setObjectName(u"label_notes")
        self.label_notes.setGeometry(QRect(20, 110, 101, 16))
        self.textEdit_notes = QTextEdit(EditPartsForm)
        self.textEdit_notes.setObjectName(u"textEdit_notes")
        self.textEdit_notes.setGeometry(QRect(20, 130, 411, 111))
        self.pushButton_edit_type = QPushButton(EditPartsForm)
        self.pushButton_edit_type.setObjectName(u"pushButton_edit_type")
        self.pushButton_edit_type.setGeometry(QRect(330, 20, 101, 24))
        self.pushButton_edit_vendor = QPushButton(EditPartsForm)
        self.pushButton_edit_vendor.setObjectName(u"pushButton_edit_vendor")
        self.pushButton_edit_vendor.setGeometry(QRect(330, 50, 101, 24))
        self.pushButton_save = QPushButton(EditPartsForm)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(20, 250, 411, 31))

        self.retranslateUi(EditPartsForm)

        QMetaObject.connectSlotsByName(EditPartsForm)
    # setupUi

    def retranslateUi(self, EditPartsForm):
        EditPartsForm.setWindowTitle(QCoreApplication.translate("EditPartsForm", u"Dialog", None))
        self.label_type.setText(QCoreApplication.translate("EditPartsForm", u"\u0422\u0438\u043f", None))
        self.label_vendor.setText(QCoreApplication.translate("EditPartsForm", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None))
        self.label_name.setText(QCoreApplication.translate("EditPartsForm", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_notes.setText(QCoreApplication.translate("EditPartsForm", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.pushButton_edit_type.setText(QCoreApplication.translate("EditPartsForm", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_edit_vendor.setText(QCoreApplication.translate("EditPartsForm", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_save.setText(QCoreApplication.translate("EditPartsForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

