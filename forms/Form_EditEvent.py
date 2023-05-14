# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_EditEvent.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_EditEventForm(object):
    def setupUi(self, EditEventForm):
        if not EditEventForm.objectName():
            EditEventForm.setObjectName(u"EditEventForm")
        EditEventForm.resize(464, 207)
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        EditEventForm.setFont(font)
        self.verticalLayout = QVBoxLayout(EditEventForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_type_event = QLabel(EditEventForm)
        self.label_type_event.setObjectName(u"label_type_event")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(True)
        self.label_type_event.setFont(font1)

        self.horizontalLayout.addWidget(self.label_type_event)

        self.cmb_type_event = QComboBox(EditEventForm)
        self.cmb_type_event.addItem("")
        self.cmb_type_event.addItem("")
        self.cmb_type_event.setObjectName(u"cmb_type_event")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_type_event.sizePolicy().hasHeightForWidth())
        self.cmb_type_event.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.cmb_type_event)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_type_part = QLabel(EditEventForm)
        self.label_type_part.setObjectName(u"label_type_part")
        self.label_type_part.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_type_part)

        self.cmb_type_part = QComboBox(EditEventForm)
        self.cmb_type_part.setObjectName(u"cmb_type_part")
        sizePolicy.setHeightForWidth(self.cmb_type_part.sizePolicy().hasHeightForWidth())
        self.cmb_type_part.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.cmb_type_part)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_part = QLabel(EditEventForm)
        self.label_part.setObjectName(u"label_part")
        self.label_part.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_part)

        self.cmb_part = QComboBox(EditEventForm)
        self.cmb_part.setObjectName(u"cmb_part")
        sizePolicy.setHeightForWidth(self.cmb_part.sizePolicy().hasHeightForWidth())
        self.cmb_part.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.cmb_part)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_date_time = QLabel(EditEventForm)
        self.label_date_time.setObjectName(u"label_date_time")
        self.label_date_time.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_date_time)

        self.dte_date_time = QDateTimeEdit(EditEventForm)
        self.dte_date_time.setObjectName(u"dte_date_time")
        self.dte_date_time.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))

        self.horizontalLayout_3.addWidget(self.dte_date_time)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_qty = QLabel(EditEventForm)
        self.label_qty.setObjectName(u"label_qty")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_qty.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_qty)

        self.edit_qty = QLineEdit(EditEventForm)
        self.edit_qty.setObjectName(u"edit_qty")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.edit_qty.setFont(font3)

        self.horizontalLayout_4.addWidget(self.edit_qty)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.btn_save = QPushButton(EditEventForm)
        self.btn_save.setObjectName(u"btn_save")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        self.btn_save.setFont(font4)
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"font: 10pt \"Arial\";\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(2, 144, 0, 150);\n"
"color:white;\n"
"}")

        self.verticalLayout.addWidget(self.btn_save)


        self.retranslateUi(EditEventForm)

        self.cmb_type_event.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(EditEventForm)
    # setupUi

    def retranslateUi(self, EditEventForm):
        EditEventForm.setWindowTitle(QCoreApplication.translate("EditEventForm", u"\u041d\u043e\u0432\u043e\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u0435", None))
        self.label_type_event.setText(QCoreApplication.translate("EditEventForm", u"\u0422\u0438\u043f \u0441\u043e\u0431\u044b\u0442\u0438\u044f:", None))
        self.cmb_type_event.setItemText(0, QCoreApplication.translate("EditEventForm", u"\u041f\u0440\u0438\u0445\u043e\u0434", None))
        self.cmb_type_event.setItemText(1, QCoreApplication.translate("EditEventForm", u"\u0420\u0430\u0441\u0445\u043e\u0434", None))

        self.cmb_type_event.setPlaceholderText(QCoreApplication.translate("EditEventForm", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.label_type_part.setText(QCoreApplication.translate("EditEventForm", u"\u0422\u0438\u043f \u0437\u0430\u043f. \u0447\u0430\u0441\u0442\u0438", None))
        self.cmb_type_part.setPlaceholderText(QCoreApplication.translate("EditEventForm", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f \u0437\u0430\u043f. \u0447\u0430\u0441\u0442\u0438", None))
        self.label_part.setText(QCoreApplication.translate("EditEventForm", u"\u0417\u0430\u043f. \u0447\u0430\u0441\u0442\u044c:", None))
        self.cmb_part.setPlaceholderText(QCoreApplication.translate("EditEventForm", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0437\u0430\u043f. \u0447\u0430\u0441\u0442\u044c", None))
        self.label_date_time.setText(QCoreApplication.translate("EditEventForm", u"\u0414\u0430\u0442\u0430, \u0432\u0440\u0435\u043c\u044f", None))
        self.label_qty.setText(QCoreApplication.translate("EditEventForm", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.btn_save.setText(QCoreApplication.translate("EditEventForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

