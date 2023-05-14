import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

from forms.Form_Main import Ui_MainForm
from forms.Form_refParts import Ui_RefPartsForm
from forms.Form_EditEvent import Ui_EditEventForm
from DatabaseWorker import Data
import Utils


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
        self.load_parts(0)

        # Настройка интерфейса
        self.ui.btn_open_refParts.clicked.connect(self.on_click_open_ref_parts)
        self.ui.btn_add.clicked.connect(self.on_click_edit_event)
        self.ui.btn_edit.clicked.connect(self.on_click_edit_event)
        self.ui.btn_delete.clicked.connect(self.on_click_delete_event)

        self.ui.comboBox_category.currentIndexChanged.connect(self.load_parts)


    def on_click_open_ref_parts(self):
        self.window_refParts = RefPartsForm()
        self.window_refParts.show()

    def on_click_edit_event(self):
        self.window_EditEvent = EditEventForm()
        sender = self.sender()
        self.window_EditEvent.show()
        if sender.objectName() == "btn_add":
            self.window_EditEvent.setWindowTitle("Добавление события")
        else:
            self.window_EditEvent.setWindowTitle("Редактирование события")

    def on_click_delete_event(self):
        print('on_click_delete_event')

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
        idcat = self.ui.comboBox_category.itemData(index)
        if idcat:
            parts = self.conn.get_parts(int(idcat))
            for part in parts:
                self.ui.comboBox_parts.addItem(part[1], part[0])


# Форма справочника зап частей
class RefPartsForm(QMainWindow):
    def __init__(self):
        super(RefPartsForm, self).__init__()
        self.ui = Ui_RefPartsForm()
        self.ui.setupUi(self)
        self.conn = Data()
        self.load_refparts()

        self.ui.btn_add.clicked.connect(self.on_click_edit_part)
        self.ui.btn_edit.clicked.connect(self.on_click_edit_part)
        self.ui.btn_del.clicked.connect(self.on_click_delete_part)

    def on_click_edit_part(self):
        print('on_click_edit_part')

    def on_click_delete_part(self):
        print('on_click_delete_part')

    def load_refparts(self):
        model = self.conn.get_table_refparts()
        self.ui.tableView.setModel(model)
        # Включаем чередование цветов строк
        self.ui.tableView.setAlternatingRowColors(True)
        # Настраиваем ширину колонок под содержимое
        self.ui.tableView.resizeColumnsToContents()
        #delegate = Utils.CustomDelegate()
        #self.ui.tableView.setItemDelegate(delegate)


# Форма добавления/редактирования событий по складу
class EditEventForm(QDialog):
    def __init__(self):
        super(EditEventForm, self).__init__()
        self.ui = Ui_EditEventForm()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()

    sys.exit(app.exec())
