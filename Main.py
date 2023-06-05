import sys
import PySide6
import sqlite3
import typing
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QCompleter
from PySide6 import QtCore
from PySide6.QtCore import QDate, QTime, QDateTime

from forms.Form_Main import Ui_MainForm
from forms.Unit_refParts import RefPartsForm
from forms.Unit_EditEvent import EditEventForm
from DatabaseWorker import Data


# Главная форма приложения
class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        # Подклюбчение к БД
        self.conn = Data()

        # Настройка контролов
        self.ui.dte_start_period.setDateTime(
            QDateTime(QDate.currentDate().year(), QDate.currentDate().month(), 1, 0, 0, 0)
        )
        self.ui.dte_end_period.setDate(QDate.currentDate())
        self.ui.dte_end_period.setTime(QTime(23, 59, 59))
        self.ui.checkbox_all_period.setChecked(False)

        # Загрузка данных из БД
        self.load_all_data()

        # Загрузка данных в контролы
        self.on_changed_category(self.ui.cmb_category.currentIndex())
        self.on_changed_parts(self.ui.cmb_parts.currentIndex())

        self.ui.btn_update_all_data.clicked.connect(self.load_all_data)
        self.ui.checkbox_all_period.clicked.connect(self.on_click_all_period)
        self.ui.btn_open_refParts.clicked.connect(self.on_click_open_ref_parts)
        self.ui.btn_add.clicked.connect(self.on_click_edit_event)
        self.ui.btn_edit.clicked.connect(self.on_click_edit_event)
        self.ui.btn_delete.clicked.connect(self.on_click_delete_event)

        self.ui.cmb_category.currentIndexChanged.connect(self.on_changed_category)
        self.ui.cmb_parts.currentIndexChanged.connect(self.on_changed_parts)

    def on_click_all_period(self):
        if self.sender().isChecked():
            self.ui.dte_start_period.close()
            self.ui.dte_end_period.close()
        else:
            self.ui.dte_start_period.show()
            self.ui.dte_end_period.show()

    def on_click_open_ref_parts(self):
        self.window_refParts = RefPartsForm()
        self.window_refParts.show()

    def on_click_edit_event(self):
        sender = self.sender()
        if sender.objectName() == "btn_add":
            self.window_EditEvent = EditEventForm(self.load_wrkevents, -1)
            self.window_EditEvent.setWindowTitle("Добавление события")
        else:
            index_row = self.ui.tableView.currentIndex().row()
            row_items = self.ui.tableView.model().get_row_items(index_row)
            id_row = row_items[0]

            self.window_EditEvent = EditEventForm(self.load_wrkevents, id_row)
            self.window_EditEvent.setWindowTitle("Редактирование события")

            self.window_EditEvent.edit_ui_data(row_items)

        self.window_EditEvent.exec()

    def on_click_delete_event(self):
        result = QMessageBox.warning(self, "Удаление записи", "Внимание! Вы уверены что хотите удалить запись?",
                                     QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Cancel)
        if result == QMessageBox.StandardButton.Ok:
            index_row = self.ui.tableView.currentIndex().row()
            row_items = self.ui.tableView.model().get_row_items(index_row)
            id_row = row_items[0]
            self.conn.delete_event_query(int(id_row))
            self.load_wrkevents()

    def on_changed_category(self, index):
        if index > -1:
            id_cat = self.ui.cmb_category.itemData(index)
            if id_cat:
                self.load_category_detail(id_cat)
        else:
            self.load_category_detail(-1)
        self.load_parts(index)

    def on_changed_parts(self, index):
        if index > -1:
            idpart = self.ui.cmb_parts.itemData(index)
            if idpart:
                self.load_part_detail(idpart)
        else:
            self.load_part_detail(-1)

    def load_wrkevents(self):
        model = self.conn.get_table_wrkevents()
        self.ui.tableView.setModel(model)
        # Включаем чередование цветов строк
        self.ui.tableView.setAlternatingRowColors(True)
        # Настраиваем ширину колонок под содержимое
        self.ui.tableView.resizeColumnsToContents()

    def load_totals(self):
        self.ui.data_count_all.setText(self.conn.total_balance())
        self.ui.data_count_in.setText(self.conn.total_income())
        self.ui.data_count_exp.setText(self.conn.total_outcome())

    def load_categories(self):
        self.ui.cmb_category.clear()
        categories = self.conn.get_categories()
        for category in categories:
            self.ui.cmb_category.addItem(category[1], category[0])
        completer = QCompleter([item[1] for item in categories])
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.cmb_category.setCompleter(completer)

    def load_parts(self, index):
        self.ui.cmb_parts.clear()
        if index > -1:
            idcat = self.ui.cmb_category.itemData(index)
            if idcat:
                parts = self.conn.get_parts(int(idcat))
                for part in parts:
                    self.ui.cmb_parts.addItem(part[1], part[0])
                completer = QCompleter([item[1] for item in parts])
                completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
                self.ui.cmb_parts.setCompleter(completer)

    def load_all_data(self):
        if not self.ui.checkbox_all_period.isChecked():
            start = self.ui.dte_start_period.dateTime().toString('yyyy-MM-dd hh:mm:ss')
            end = self.ui.dte_end_period.dateTime().toString('yyyy-MM-dd hh:mm:ss')
            self.conn.period.update({'start': start, 'end': end})
        else:
            self.conn.period.update({'start': '', 'end': ''})
        self.load_wrkevents()
        self.load_categories()
        self.load_totals()

    def load_category_detail(self, id):
        self.ui.data_in_category.setText(self.conn.income_by_category(id))
        self.ui.data_exp_category.setText(self.conn.outcome_by_category(id))

    def load_part_detail(self, id):
        self.ui.data_in_parts.setText(self.conn.income_by_part(id))
        self.ui.data_exp_parts.setText(self.conn.outcome_by_part(id))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()

    sys.exit(app.exec())
