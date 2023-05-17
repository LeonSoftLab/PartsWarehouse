from PySide6 import QtWidgets
from PySide6.QtGui import QStandardItemModel, QStandardItem
import sqlite3

import Utils


class Data:
    def __init__(self):
        super(Data, self).__init__()
        # Получение данных из базы SQLite
        try:
            self.connection = sqlite3.connect('db\database.db')
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка инициализации базы данных", f"Ошибка: {e}")

        # TODO: Create Objects in Database like query.exec('CREATE TABLE IF NOT EXISTS "refTypeParts" (')

    def add_event_query(self, type, idpart, datetime, qty):
        self.cursor.execute("INSERT INTO wrkEvents (Type, idPart, DateTime, Qty) VALUES (?, ?, ?, ?)",
                            (type, idpart, datetime, qty))
        self.connection.commit()

    def update_event_query(self, type, idpart, datetime, qty, id):
        self.cursor.execute("UPDATE wrkEvents SET Type=?, idPart=?, DateTime=?, Qty=? WHERE id=?",
                            (type, idpart, datetime, qty, id))
        self.connection.commit()

    def delete_part_query(self, id):
        self.cursor.execute("DELETE FROM wrkEvents WHERE id=?",
                            (id,))
        self.connection.commit()

    def add_part_query(self, idcategory, idvendor, name, notes):
        self.cursor.execute("INSERT INTO refParts (idCategory, idVendor, Name, Notes)VALUES (?, ?, ?, ?)",
                            (idcategory, idvendor, name, notes))
        self.connection.commit()

    def update_part_query(self, idcategory, idvendor, name, notes, id):
        self.cursor.execute("UPDATE refParts SET idCategory=?, idVendor=?, Name=?, Notes=? WHERE id=?",
                            (idcategory, idvendor, name, notes, id))
        self.connection.commit()

    def delete_part_query(self, id):
        self.cursor.execute("DELETE FROM refParts WHERE id=?",
                            (id,))
        self.connection.commit()

    def get_total(self, column, filter=None, value=None):
        sql_query = f"SELECT SUM(wrk.{column}) FROM wrkEvents wrk "
        sql_query += " INNER JOIN refParts rP on rP.id = wrk.idPart "
        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"
            query = self.cursor.execute(sql_query, (value,)).fetchone()
        else:
            query = self.cursor.execute(sql_query).fetchone()

        if query is not None:
            return str(query[0])

        return '0'

    def get_total_by_partcat(self, column, filtr, valuefiltr, valuetype):
        sql_query = f"SELECT SUM(wrk.{column}) FROM wrkEvents wrk "
        sql_query += " INNER JOIN refParts rP on rP.id = wrk.idPart "
        sql_query += f" WHERE {filtr} = ? AND Type = ? "
        query = self.cursor.execute(sql_query, (valuefiltr, valuetype)).fetchone()
        if query is not None:
            return str(query[0])

        return '0'

    def get_table_wrkevents(self):
        data = self.cursor.execute("SELECT "
                                   "   wrk.id as 'Код записи', "
                                   "   wrk.Type as 'Тип события', "
                                   "   rP.idCategory as 'Код категории', "
                                   "   rC.Name as 'Категория зап. части', "
                                   "   wrk.idPart as 'Код зап. части', "
                                   "   rP.Name as 'Наименование зап части', "
                                   "   wrk.DateTime as 'Дата/время события', "
                                   "   wrk.Qty as 'Количество' "
                                   "FROM wrkEvents wrk "
                                   "  INNER JOIN refParts rP on rP.id = wrk.idPart "
                                   "  INNER JOIN refCategories rC on rC.id = rP.idCategory "
                                   ).fetchall()
        headers = [column[0] for column in self.cursor.description]
        model = Utils.CustomTableModel(data, headers)

        return model

    def get_table_refparts(self):
        data = self.cursor.execute("SELECT "
                                   "   rP.id as 'Код', "
                                   "   rP.idCategory as 'Код категории', "
                                   "   rC.Name as 'Категория зап. части', "
                                   "   rP.idVendor as 'Код поставщика', "
                                   "   rV.Name as 'Поставщик зап. части', "
                                   "   rP.Name as 'Наименование зап. части', "
                                   "   rP.Notes as 'Описание зап. части' "
                                   " FROM refParts rP "
                                   "   INNER JOIN refCategories rC on rC.id = rP.idCategory "
                                   "   INNER JOIN refVendors rV on rV.id = rP.idVendor "
                                   ).fetchall()
        headers = [column[0] for column in self.cursor.description]
        model = Utils.CustomTableModel(data, headers)

        return model

    def get_categories(self):
        data = self.cursor.execute("SELECT id, Name "
                                   "FROM refCategories "
                                   ).fetchall()

        return data

    def get_parts(self, idcat=None):
        sql_query = "SELECT id, Name FROM refParts "
        if idcat is not None:
            sql_query += " WHERE idCategory = ?"
            data = self.cursor.execute(sql_query, (idcat,)).fetchall()
        else:
            data = self.cursor.execute(sql_query).fetchall()

        return data

    def total_balance(self):
        return self.get_total(column="Qty")

    def total_income(self):
        return self.get_total(column="Qty", filter="Type", value="Приход")

    def total_outcome(self):
        return self.get_total(column="Qty", filter="Type", value="Расход")

    def income_by_category(self, idcat):
        return self.get_total_by_partcat(column="Qty", filtr="idCategory", valuefiltr=idcat, valuetype="Приход")

    def outcome_by_category(self, idcat):
        return self.get_total_by_partcat(column="Qty", filtr="idCategory", valuefiltr=idcat, valuetype="Расход")

    def income_by_part(self, idpart):
        return self.get_total_by_partcat(column="Qty", filtr="idPart", valuefiltr=idpart, valuetype="Приход")

    def outcome_by_part(self, idpart):
        return self.get_total_by_partcat(column="Qty", filtr="idPart", valuefiltr=idpart, valuetype="Расход")
