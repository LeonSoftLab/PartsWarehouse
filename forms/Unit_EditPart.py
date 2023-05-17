from PySide6.QtWidgets import QDialog, QMessageBox

from DatabaseWorker import Data
from forms.Form_EditPart import Ui_EditPartForm
from forms.Form_AddName import Ui_AddNameForm

# Форма добавления/редактирования зап. частей
class EditPartForm(QDialog):
    def __init__(self, refresh, id_rec):
        super(EditPartForm, self).__init__()
        self.func_refresh = refresh
        self.id_rec = id_rec
        self.ui = Ui_EditPartForm()
        self.ui.setupUi(self)
        self.conn = Data()
        self.load_categories()
        self.load_vendors()

        self.ui.cmb_category.currentIndexChanged.connect(self.on_changed_category)
        self.ui.cmb_vendor.currentIndexChanged.connect(self.on_changed_vendor)
        self.ui.btn_save.clicked.connect(self.on_click_save)
        self.ui.btn_add_category.clicked.connect(self.on_click_add_category)
        self.ui.btn_add_vendor.clicked.connect(self.on_click_add_vendor)

    def load_categories(self):
        self.ui.cmb_category.clear()
        categories = self.conn.get_categories()
        for category in categories:
            self.ui.cmb_category.addItem(category[1], category[0])

    def load_vendors(self):
        self.ui.cmb_vendor.clear()
        vendors = self.conn.get_vendors()
        for vendor in vendors:
            self.ui.cmb_vendor.addItem(vendor[1], vendor[0])

    def on_changed_category(self, index):
        pass

    def on_changed_vendor(self, index):
        pass

    def edit_ui_data(self, row_data):
        self.ui.cmb_category.setCurrentIndex(
            self.ui.cmb_category.findData(row_data[1]))
        self.ui.cmb_vendor.setCurrentIndex(
            self.ui.cmb_vendor.findData(row_data[3]))
        self.ui.edit_name.setText(str(row_data[5]))
        self.ui.edit_notes.setPlainText(str(row_data[6]))

    def on_click_add_category(self):
        window_AddName = QDialog()
        ui_AddName = Ui_AddNameForm()
        ui_AddName.setupUi(window_AddName)
        window_AddName.setWindowTitle("Добавление категории")
        window_AddName.exec()
        new_category = ui_AddName.edit_name.text()
        self.conn.add_category_query(new_category, "")

    def on_click_add_vendor(self):
        window_AddName = QDialog()
        ui_AddName = Ui_AddNameForm()
        ui_AddName.setupUi(window_AddName)
        window_AddName.setWindowTitle("Добавление поставщика")
        window_AddName.exec()
        new_category = ui_AddName.edit_name.text()
        self.conn.add_vendor_query(new_category, "")

    def on_click_save(self):
        if all(num > -1 for num in [self.ui.cmb_category.currentIndex(),
                                    self.ui.cmb_vendor.currentIndex()]
               ) and self.ui.edit_name.text() != "":
            idcategory = self.ui.cmb_category.itemData(self.ui.cmb_category.currentIndex())
            idvendor = self.ui.cmb_vendor.itemData(self.ui.cmb_vendor.currentIndex())
            name = self.ui.edit_name.text()
            notes = self.ui.edit_notes.toPlainText()
            if self.id_rec < 0:
                self.conn.add_part_query(idcategory, idvendor, name, notes)
            else:
                self.conn.update_part_query(idcategory, idvendor, name, notes, self.id_rec)
            self.func_refresh()
            self.close()
        else:
            QMessageBox.warning(self, "Редактирование зап. части",
                                "Проверьте заполнение всех данных на форме и попробуйте ещё раз.")
