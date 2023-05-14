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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AddNameForm(object):
    def setupUi(self, AddNameForm):
        if not AddNameForm.objectName():
            AddNameForm.setObjectName(u"AddNameForm")
        AddNameForm.resize(400, 104)
        self.verticalLayout = QVBoxLayout(AddNameForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(AddNameForm)
        self.label_name.setObjectName(u"label_name")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.label_name.setFont(font)

        self.verticalLayout.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(AddNameForm)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.verticalLayout.addWidget(self.lineEdit_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_ok = QPushButton(AddNameForm)
        self.btn_ok.setObjectName(u"btn_ok")
        font1 = QFont()
        font1.setBold(True)
        self.btn_ok.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_ok)

        self.btn_cancel = QPushButton(AddNameForm)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AddNameForm)

        QMetaObject.connectSlotsByName(AddNameForm)
    # setupUi

    def retranslateUi(self, AddNameForm):
        AddNameForm.setWindowTitle(QCoreApplication.translate("AddNameForm", u"Dialog", None))
        self.label_name.setText(QCoreApplication.translate("AddNameForm", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.btn_ok.setText(QCoreApplication.translate("AddNameForm", u"\u041e\u043a", None))
        self.btn_cancel.setText(QCoreApplication.translate("AddNameForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

