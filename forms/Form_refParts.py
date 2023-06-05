# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_refParts.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_RefPartsForm(object):
    def setupUi(self, RefPartsForm):
        if not RefPartsForm.objectName():
            RefPartsForm.setObjectName(u"RefPartsForm")
        RefPartsForm.resize(674, 560)
        self.centralwidget = QWidget(RefPartsForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(self.frame)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setStyleSheet(u"QPushButton {\n"
"font: 10pt \"Arial\";\n"
"background-color: rgba(0, 153, 255, 100);\n"
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

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_edit = QPushButton(self.frame)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setStyleSheet(u"QPushButton {\n"
"font: 10pt \"Arial\";\n"
"background-color: rgba(0, 153, 255, 100);\n"
"margin: 5px;\n"
"padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(210, 210, 0, 100);\n"
"color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(210, 210, 0, 150);\n"
"color:white;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_edit)

        self.btn_del = QPushButton(self.frame)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setStyleSheet(u"QPushButton {\n"
"font: 10pt \"Arial\";\n"
"background-color: rgba(0, 153, 255, 100);\n"
"border-style: dotted;\n"
"margin: 5px;\n"
"padding: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(207, 0, 3, 100);\n"
"color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(207, 0, 3, 150);\n"
"color:white;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_del)


        self.verticalLayout.addWidget(self.frame)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
" background-color: rgba(255, 255, 255, 30);\n"
" border: 1px solid rgba(0, 0, 0, 200);\n"
" color: black;\n"
" border-radius : 5px;\n"
"}\n"
"\n"
"QTableView::section {\n"
" background-color: rgba(30, 144, 255, 100);\n"
" color: black;\n"
" font-weight: bold;\n"
" border: 1px solid rgba(0, 0, 0, 200);\n"
" height: 40px;\n"
" border-radius : 5px;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(0, 0, 0);\n"
"    background-color: rgba(30, 144, 255, 50);\n"
"}")

        self.verticalLayout.addWidget(self.tableView)

        RefPartsForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(RefPartsForm)

        QMetaObject.connectSlotsByName(RefPartsForm)
    # setupUi

    def retranslateUi(self, RefPartsForm):
        RefPartsForm.setWindowTitle(QCoreApplication.translate("RefPartsForm", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u0437\u0430\u043f. \u0447\u0430\u0441\u0442\u0435\u0439", None))
        self.btn_add.setText(QCoreApplication.translate("RefPartsForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_edit.setText(QCoreApplication.translate("RefPartsForm", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btn_del.setText(QCoreApplication.translate("RefPartsForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

