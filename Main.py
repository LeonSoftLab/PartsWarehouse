import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox

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

        # Загрузка данных из БД
        self.load_wrkevents()
        self.load_totals()
        self.load_categories()
        self.on_changed_category(self.ui.comboBox_category.currentIndex())
        self.on_changed_parts(self.ui.comboBox_parts.currentIndex())

        # Настройка интерфейса
        self.ui.btn_open_refParts.clicked.connect(self.on_click_open_ref_parts)
        self.ui.btn_add.clicked.connect(self.on_click_edit_event)
        self.ui.btn_edit.clicked.connect(self.on_click_edit_event)
        self.ui.btn_delete.clicked.connect(self.on_click_delete_event)

        self.ui.comboBox_category.currentIndexChanged.connect(self.on_changed_category)
        self.ui.comboBox_parts.currentIndexChanged.connect(self.on_changed_parts)


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

        self.window_EditEvent.show()

    def on_click_delete_event(self):
        result = QMessageBox.warning(self, "PartsWarehouse", "Внимание! Вы уверены что хотите удалить запись?",
                                     QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Cancel)
        if result == QMessageBox.StandardButton.Ok:
            index_row = self.ui.tableView.currentIndex().row()
            row_items = self.ui.tableView.model().get_row_items(index_row)
            id_row = row_items[0]
            self.conn.delete_event_query(int(id_row))
            self.load_wrkevents()

    def on_changed_category(self, index):
        if index > -1:
            idcat = self.ui.comboBox_category.itemData(index)
            if idcat:
                self.load_category_detail(idcat)
        self.load_parts(index)

    def on_changed_parts(self, index):
        if index > -1:
            idpart = self.ui.comboBox_parts.itemData(index)
            if idpart:
                self.load_part_detail(idpart)

    def load_wrkevents(self):
        model = self.conn.get_table_wrkevents()
        self.ui.tableView.setModel(model)
        # Включаем чередование цветов строк
        self.ui.tableView.setAlternatingRowColors(True)
        # Настраиваем ширину колонок под содержимое
        self.ui.tableView.resizeColumnsToContents()
        #delegate = Utils.CustomDelegate()
        #self.ui.tableView.setItemDelegate(delegate)

    def load_totals(self):
        self.ui.data_count_all.setText(self.conn.total_balance())
        self.ui.data_count_in.setText(self.conn.total_income())
        self.ui.data_count_exp.setText(self.conn.total_outcome())

    def load_categories(self):
        self.ui.comboBox_category.clear()
        categories = self.conn.get_categories()
        for category in categories:
            self.ui.comboBox_category.addItem(category[1], category[0])

    def load_parts(self, index):
        self.ui.comboBox_parts.clear()
        if index > -1:
            idcat = self.ui.comboBox_category.itemData(index)
            if idcat:
                parts = self.conn.get_parts(int(idcat))
                for part in parts:
                    self.ui.comboBox_parts.addItem(part[1], part[0])

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
