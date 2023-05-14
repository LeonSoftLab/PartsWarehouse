# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_refVendors.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_RefVendorsForm(object):
    def setupUi(self, RefVendorsForm):
        if not RefVendorsForm.objectName():
            RefVendorsForm.setObjectName(u"RefVendorsForm")
        RefVendorsForm.resize(510, 402)
        self.verticalLayout = QVBoxLayout(RefVendorsForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(RefVendorsForm)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_edit = QPushButton(RefVendorsForm)
        self.btn_edit.setObjectName(u"btn_edit")

        self.horizontalLayout.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(RefVendorsForm)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(RefVendorsForm)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(RefVendorsForm)

        QMetaObject.connectSlotsByName(RefVendorsForm)
    # setupUi

    def retranslateUi(self, RefVendorsForm):
        RefVendorsForm.setWindowTitle(QCoreApplication.translate("RefVendorsForm", u"Dialog", None))
        self.btn_add.setText(QCoreApplication.translate("RefVendorsForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_edit.setText(QCoreApplication.translate("RefVendorsForm", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btn_delete.setText(QCoreApplication.translate("RefVendorsForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

