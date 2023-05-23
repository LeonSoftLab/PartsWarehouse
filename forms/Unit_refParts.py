from PySide6.QtWidgets import QMainWindow, QMessageBox

from forms.Form_refParts import Ui_RefPartsForm
from forms.Unit_EditPart import EditPartForm
from DatabaseWorker import Data

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
        sender = self.sender()
        if sender.objectName() == "btn_add":
            self.window_EditPart = EditPartForm(self.load_refparts, -1)
            self.window_EditPart.setWindowTitle("Добавление зап. части")
        else:
            index_row = self.ui.tableView.currentIndex().row()
            row_items = self.ui.tableView.model().get_row_items(index_row)
            id_row = row_items[0]

            self.window_EditPart = EditPartForm(self.load_refparts, id_row)
            self.window_EditPart.setWindowTitle("Редактирование зап. части")

            self.window_EditPart.edit_ui_data(row_items)

        self.window_EditPart.exec()

    def on_click_delete_part(self):
        result = QMessageBox.warning(self, "Удаление зап. части", "Внимание! Вы уверены что хотите удалить запись?",
                                     QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Cancel)
        if result == QMessageBox.StandardButton.Ok:
            index_row = self.ui.tableView.currentIndex().row()
            row_items = self.ui.tableView.model().get_row_items(index_row)
            id_row = row_items[0]
            self.conn.delete_part_query(int(id_row))
            self.load_refparts()

    def load_refparts(self):
        model = self.conn.get_table_refparts()
        self.ui.tableView.setModel(model)
        # Включаем чередование цветов строк
        self.ui.tableView.setAlternatingRowColors(True)
        # Настраиваем ширину колонок под содержимое
        self.ui.tableView.resizeColumnsToContents()