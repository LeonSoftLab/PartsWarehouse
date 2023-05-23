# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_Main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.resize(914, 741)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        MainForm.setFont(font)
        self.centralwidget = QWidget(MainForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_top_2 = QFrame(self.centralwidget)
        self.frame_top_2.setObjectName(u"frame_top_2")
        self.frame_top_2.setStyleSheet(u"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;")
        self.horizontalLayout_10 = QHBoxLayout(self.frame_top_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_work_period = QLabel(self.frame_top_2)
        self.label_work_period.setObjectName(u"label_work_period")
        self.label_work_period.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_10.addWidget(self.label_work_period)

        self.dte_start_period = QDateTimeEdit(self.frame_top_2)
        self.dte_start_period.setObjectName(u"dte_start_period")
        self.dte_start_period.setStyleSheet(u"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"margin: 2px;\n"
"padding: 3px;")

        self.horizontalLayout_10.addWidget(self.dte_start_period)

        self.dte_end_period = QDateTimeEdit(self.frame_top_2)
        self.dte_end_period.setObjectName(u"dte_end_period")
        self.dte_end_period.setStyleSheet(u"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"margin: 2px;\n"
"padding: 3px;")

        self.horizontalLayout_10.addWidget(self.dte_end_period)

        self.checkbox_all_period = QCheckBox(self.frame_top_2)
        self.checkbox_all_period.setObjectName(u"checkbox_all_period")
        self.checkbox_all_period.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_10.addWidget(self.checkbox_all_period)

        self.btn_update_all_data = QPushButton(self.frame_top_2)
        self.btn_update_all_data.setObjectName(u"btn_update_all_data")
        self.btn_update_all_data.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_10.addWidget(self.btn_update_all_data)


        self.verticalLayout.addWidget(self.frame_top_2)

        self.frame_middle_2 = QFrame(self.centralwidget)
        self.frame_middle_2.setObjectName(u"frame_middle_2")
        self.horizontalLayout_12 = QHBoxLayout(self.frame_middle_2)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_middle_left = QFrame(self.frame_middle_2)
        self.frame_middle_left.setObjectName(u"frame_middle_left")
        self.frame_middle_left.setMinimumSize(QSize(230, 0))
        self.frame_middle_left.setStyleSheet(u"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;\n"
"padding: 0px;\n"
"margin: 0px;")
        self.verticalLayout_2 = QVBoxLayout(self.frame_middle_left)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_count_all = QLabel(self.frame_middle_left)
        self.label_count_all.setObjectName(u"label_count_all")
        self.label_count_all.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_11.addWidget(self.label_count_all)

        self.data_count_all = QLabel(self.frame_middle_left)
        self.data_count_all.setObjectName(u"data_count_all")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.data_count_all.setFont(font1)
        self.data_count_all.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-weight: bold;\n"
"font-family: \"Arial\";\n"
"font-size: 14pt;\n"
"border: none;")

        self.horizontalLayout_11.addWidget(self.data_count_all)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_count_in = QLabel(self.frame_middle_left)
        self.label_count_in.setObjectName(u"label_count_in")
        self.label_count_in.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_count_in)

        self.data_count_in = QLabel(self.frame_middle_left)
        self.data_count_in.setObjectName(u"data_count_in")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.data_count_in.setFont(font2)
        self.data_count_in.setStyleSheet(u"background-color: none;\n"
"color: green;\n"
"font-weight: bold;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.data_count_in)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_count_exp = QLabel(self.frame_middle_left)
        self.label_count_exp.setObjectName(u"label_count_exp")
        self.label_count_exp.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.label_count_exp)

        self.data_count_exp = QLabel(self.frame_middle_left)
        self.data_count_exp.setObjectName(u"data_count_exp")
        self.data_count_exp.setFont(font2)
        self.data_count_exp.setStyleSheet(u"background-color: none;\n"
"color: red;\n"
"font-weight: bold;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.data_count_exp)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_12.addWidget(self.frame_middle_left)

        self.frame_middle_right = QFrame(self.frame_middle_2)
        self.frame_middle_right.setObjectName(u"frame_middle_right")
        self.verticalLayout_5 = QVBoxLayout(self.frame_middle_right)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_right1 = QFrame(self.frame_middle_right)
        self.frame_right1.setObjectName(u"frame_right1")
        self.frame_right1.setStyleSheet(u"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_right1)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.label_exp_category = QLabel(self.frame_right1)
        self.label_exp_category.setObjectName(u"label_exp_category")
        self.label_exp_category.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_exp_category)

        self.data_exp_category = QLabel(self.frame_right1)
        self.data_exp_category.setObjectName(u"data_exp_category")
        self.data_exp_category.setMinimumSize(QSize(50, 0))
        self.data_exp_category.setFont(font2)
        self.data_exp_category.setStyleSheet(u"background-color: none;\n"
"color: red;\n"
"font-weight: bold;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.data_exp_category)

        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.label_in_category = QLabel(self.frame_right1)
        self.label_in_category.setObjectName(u"label_in_category")
        self.label_in_category.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.label_in_category)

        self.data_in_category = QLabel(self.frame_right1)
        self.data_in_category.setObjectName(u"data_in_category")
        self.data_in_category.setMinimumSize(QSize(50, 0))
        self.data_in_category.setFont(font2)
        self.data_in_category.setStyleSheet(u"background-color: none;\n"
"color: green;\n"
"font-weight: bold;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.data_in_category)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.cmb_category = QComboBox(self.frame_right1)
        self.cmb_category.setObjectName(u"cmb_category")
        self.cmb_category.setMinimumSize(QSize(350, 0))
        self.cmb_category.setStyleSheet(u"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"margin: 2px;\n"
"padding: 3px;")

        self.horizontalLayout_6.addWidget(self.cmb_category)

        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_5.addWidget(self.frame_right1)

        self.frame_right2 = QFrame(self.frame_middle_right)
        self.frame_right2.setObjectName(u"frame_right2")
        self.frame_right2.setStyleSheet(u"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;")
        self.horizontalLayout_9 = QHBoxLayout(self.frame_right2)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.label_exp_parts = QLabel(self.frame_right2)
        self.label_exp_parts.setObjectName(u"label_exp_parts")
        self.label_exp_parts.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_8.addWidget(self.label_exp_parts)

        self.data_exp_parts = QLabel(self.frame_right2)
        self.data_exp_parts.setObjectName(u"data_exp_parts")
        self.data_exp_parts.setMinimumSize(QSize(50, 0))
        self.data_exp_parts.setFont(font2)
        self.data_exp_parts.setStyleSheet(u"background-color: none;\n"
"color: red;\n"
"font-weight: bold;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_8.addWidget(self.data_exp_parts)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.label_in_parts = QLabel(self.frame_right2)
        self.label_in_parts.setObjectName(u"label_in_parts")
        self.label_in_parts.setStyleSheet(u"background-color: none;\n"
"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_7.addWidget(self.label_in_parts)

        self.data_in_parts = QLabel(self.frame_right2)
        self.data_in_parts.setObjectName(u"data_in_parts")
        self.data_in_parts.setMinimumSize(QSize(50, 0))
        self.data_in_parts.setFont(font2)
        self.data_in_parts.setStyleSheet(u"background-color: none;\n"
"color: green;\n"
"font-weight: bold;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"border: none;")

        self.horizontalLayout_7.addWidget(self.data_in_parts)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.cmb_parts = QComboBox(self.frame_right2)
        self.cmb_parts.setObjectName(u"cmb_parts")
        self.cmb_parts.setMinimumSize(QSize(350, 0))
        self.cmb_parts.setStyleSheet(u"color: black;\n"
"font-family: \"Arial\";\n"
"font-size: 12pt;\n"
"margin: 2px;\n"
"padding: 3px;")

        self.horizontalLayout_9.addWidget(self.cmb_parts)

        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_5.addWidget(self.frame_right2)


        self.horizontalLayout_12.addWidget(self.frame_middle_right)

        self.horizontalLayout_12.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_middle_2)

        self.frame_middle = QFrame(self.centralwidget)
        self.frame_middle.setObjectName(u"frame_middle")
        self.frame_middle.setStyleSheet(u"color: black;\n"
"border: 1px solid rgba(0, 0, 0, 200);\n"
"border-radius : 5px;")
        self.horizontalLayout = QHBoxLayout(self.frame_middle)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(self.frame_middle)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(120, 0))
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

        self.btn_edit = QPushButton(self.frame_middle)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setMinimumSize(QSize(120, 0))
        self.btn_edit.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.frame_middle)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(120, 0))
        self.btn_delete.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_open_refParts = QPushButton(self.frame_middle)
        self.btn_open_refParts.setObjectName(u"btn_open_refParts")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open_refParts.sizePolicy().hasHeightForWidth())
        self.btn_open_refParts.setSizePolicy(sizePolicy)
        self.btn_open_refParts.setMinimumSize(QSize(140, 0))
        self.btn_open_refParts.setMaximumSize(QSize(16777215, 16777215))
        self.btn_open_refParts.setBaseSize(QSize(0, 0))
        self.btn_open_refParts.setLayoutDirection(Qt.LeftToRight)
        self.btn_open_refParts.setStyleSheet(u"QPushButton {\n"
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
        self.btn_open_refParts.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_open_refParts)


        self.verticalLayout.addWidget(self.frame_middle)

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
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableView.setAutoScroll(True)

        self.verticalLayout.addWidget(self.tableView)

        MainForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"\u041e\u0441\u0442\u0430\u0442\u043a\u0438 \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435 \u0417/\u0427", None))
        self.label_work_period.setText(QCoreApplication.translate("MainForm", u"\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434:", None))
        self.checkbox_all_period.setText(QCoreApplication.translate("MainForm", u"\u0412\u0435\u0441\u044c \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.btn_update_all_data.setText(QCoreApplication.translate("MainForm", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_count_all.setText(QCoreApplication.translate("MainForm", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u0441\u0435\u0433\u043e", None))
        self.data_count_all.setText(QCoreApplication.translate("MainForm", u"0", None))
        self.label_count_in.setText(QCoreApplication.translate("MainForm", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0438\u0445\u043e\u0434\u0430", None))
        self.data_count_in.setText(QCoreApplication.translate("MainForm", u"0", None))
        self.label_count_exp.setText(QCoreApplication.translate("MainForm", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u0430\u0441\u0445\u043e\u0434\u0430", None))
        self.data_count_exp.setText(QCoreApplication.translate("MainForm", u"0", None))
        self.label_exp_category.setText(QCoreApplication.translate("MainForm", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b \u043f\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.data_exp_category.setText(QCoreApplication.translate("MainForm", u"0", None))
        self.label_in_category.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u0445\u043e\u0434\u044b \u043f\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.data_in_category.setText(QCoreApplication.translate("MainForm", u"0", None))
        self.cmb_category.setPlaceholderText(QCoreApplication.translate("MainForm", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.label_exp_parts.setText(QCoreApplication.translate("MainForm", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b \u043f\u043e \u0442\u043e\u0432\u0430\u0440\u0443", None))
        self.data_exp_parts.setText(QCoreApplication.translate("MainForm", u"0", None))
        self.label_in_parts.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u0445\u043e\u0434\u044b \u043f\u043e \u0442\u043e\u0432\u0430\u0440\u0443", None))
        self.data_in_parts.setText(QCoreApplication.translate("MainForm", u"0", None))
        self.cmb_parts.setPlaceholderText(QCoreApplication.translate("MainForm", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0437\u0430\u043f. \u0447\u0430\u0441\u0442\u044c", None))
        self.btn_add.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_edit.setText(QCoreApplication.translate("MainForm", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btn_delete.setText(QCoreApplication.translate("MainForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btn_open_refParts.setText(QCoreApplication.translate("MainForm", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u0417/\u0427", None))
    # retranslateUi

