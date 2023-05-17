from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6 import QtCore
from datetime import datetime

from forms.Form_EditEvent import Ui_EditEventForm
from DatabaseWorker import Data

# Форма добавления/редактирования событий по складу
class EditEventForm(QDialog):
    def __init__(self, refresh, id_rec):
        super(EditEventForm, self).__init__()
        self.func_refresh = refresh
        self.id_rec = id_rec
        self.ui = Ui_EditEventForm()
        self.ui.setupUi(self)
        self.conn = Data()
        self.load_categories()

        self.on_changed_category(self.ui.cmb_category.currentIndex())
        self.on_changed_parts(self.ui.cmb_part.currentIndex())

        self.ui.cmb_category.currentIndexChanged.connect(self.on_changed_category)
        self.ui.cmb_part.currentIndexChanged.connect(self.on_changed_parts)
        self.ui.btn_save.clicked.connect(self.on_click_save)

        self.ui.dte_date_time.setDateTime(datetime.now())

    def load_categories(self):
        self.ui.cmb_category.clear()
        categories = self.conn.get_categories()
        for category in categories:
            self.ui.cmb_category.addItem(category[1], category[0])

    def load_parts(self, index):
        if index > -1:
            self.ui.cmb_part.clear()
            idcat = self.ui.cmb_category.itemData(index)
            if idcat:
                parts = self.conn.get_parts(int(idcat))
                for part in parts:
                    self.ui.cmb_part.addItem(part[1], part[0])

    def on_changed_category(self, index):
        self.load_parts(index)

    def on_changed_parts(self, index):
        pass

    def edit_ui_data(self, row_data):
        self.ui.cmb_type_event.setCurrentIndex(
            self.ui.cmb_type_event.findText(row_data[1]))
        self.ui.cmb_category.setCurrentIndex(
            self.ui.cmb_category.findData(row_data[2]))
        self.ui.cmb_part.setCurrentIndex(
            self.ui.cmb_part.findData(row_data[4]))
        self.ui.dte_date_time.setDateTime(QtCore.QDateTime.fromString(row_data[6]
                                                                      , 'yyyy-MM-dd hh:mm:ss'))
        self.ui.edit_qty.setText(str(row_data[7]))

    def on_click_save(self):
        if all(num > -1 for num in [self.ui.cmb_type_event.currentIndex(),
                                    self.ui.cmb_category.currentIndex(),
                                    self.ui.cmb_part.currentIndex()]
               ) and self.ui.edit_qty.text().isdigit():
            _type = self.ui.cmb_type_event.itemText(self.ui.cmb_type_event.currentIndex())
            idpart = self.ui.cmb_part.itemData(self.ui.cmb_part.currentIndex())
            _datetime = self.ui.dte_date_time.dateTime().toString('yyyy-MM-dd hh:mm:ss')
            qty = float(self.ui.edit_qty.text())
            if self.id_rec < 0:
                self.conn.add_event_query(_type, idpart, _datetime, qty)
            else:
                self.conn.update_event_query(_type, idpart, _datetime, qty, self.id_rec)
            self.func_refresh()
            self.close()
        else:
            QMessageBox.warning(self, "Редактирование движения по складу",
                                "Проверьте заполнение всех данных на форме и попробуйте ещё раз.")
