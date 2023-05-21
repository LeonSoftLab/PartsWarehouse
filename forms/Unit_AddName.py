from PySide6.QtWidgets import QDialog, QMessageBox

from forms.Form_AddName import Ui_AddNameForm


# Форма добавления/редактирования наименований
class AddNameForm(QDialog):
    def __init__(self, id_rec):
        super(AddNameForm, self).__init__()
        self.id_rec = id_rec
        self.result = "Cancel"
        self.ui = Ui_AddNameForm()
        self.ui.setupUi(self)

        self.ui.btn_ok.clicked.connect(self.on_click_ok)
        self.ui.btn_cancel.clicked.connect(self.on_click_cancel)

    def edit_ui_data(self, row_data):
        pass

    def on_click_ok(self):
        self.result = "Ok"
        self.close()

    def on_click_cancel(self):
        self.result = "Cancel"
        self.close()
