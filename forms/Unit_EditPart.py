from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6 import QtCore
from datetime import datetime

from DatabaseWorker import Data
from forms.Form_EditPart import Ui_EditPartForm

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

        self.on_changed_category(self.ui.cmb_cat.currentIndex())
        self.on_changed_vendor(self.ui.cmb_vendor.currentIndex())

    def on_changed_category(self, index):
        pass

    def on_changed_vendor(self, index):
        pass
