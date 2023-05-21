from PySide6.QtCore import Qt, QAbstractTableModel, QObject
from PySide6.QtWidgets import QStyledItemDelegate
from PySide6.QtGui import QColor

from typing import Optional


class CustomTableModel(QAbstractTableModel):
    def __init__(self, data, headers, parent: Optional[QObject] = None):
        super(CustomTableModel, self).__init__()
        self._data = data
        self._headers = headers
    #TODO: в модели предусмотреть работу с базой

    def rowCount(self, parent=None):
        return len(self._data) if self._data else 0

    def columnCount(self, parent=None):
        return len(self._data[0]) if self._data else 0

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data[index.row()][index.column()])
        elif role == Qt.BackgroundRole:
            return QColor('white') if index.row() % 2 == 0 else QColor(240, 240, 240)
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        elif role == Qt.BackgroundRole:
            return QColor(180, 230, 230)
        return None

    def flags(self, index):
        #if index.row() > 0:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled #| Qt.ItemIsEditable
        #elif index.column() == 1:
        #    return Qt.DecorationRole
        #else:
        #    return Qt.ItemIsSelectable

    def get_row_items(self, index):
        return self._data[index]


class EventsTableModel(QAbstractTableModel):
    def __init__(self, data, headers, parent: Optional[QObject] = None):
        super(EventsTableModel, self).__init__()
        self._data = data
        self._headers = headers
    #TODO: в модели предусмотреть работу с базой

    def rowCount(self, parent=None):
        return len(self._data) if self._data else 0

    def columnCount(self, parent=None):
        return len(self._data[0]) if self._data else 0

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data[index.row()][index.column()])
        elif role == Qt.BackgroundRole:
            return QColor(210, 250, 215) if str(self._data[index.row()][1]) == "Приход" else\
                QColor(250, 210, 215)
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        elif role == Qt.BackgroundRole:
            return QColor(180, 230, 230)
        return None

    def flags(self, index):
        #if index.row() > 0:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled #| Qt.ItemIsEditable
        #elif index.column() == 1:
        #    return Qt.DecorationRole
        #else:
        #    return Qt.ItemIsSelectable

    def get_row_items(self, index):
        return self._data[index]


class CustomDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)

        if index.row() == 0:
            # Яркий фон для шапки таблицы
            option.backgroundBrush = QColor(100, 149, 237)  # Цвет подсветки (яркий синий)
            option.palette.setColor(option.palette.Base, QColor(100, 149, 237))  # Цвет текста (белый)
        else:
            # Чередуем светло-серый фон для четных строк и белый фон для нечетных строк
            if index.row() % 2 == 0:
                option.backgroundBrush = QColor(230, 230, 230)  # Светло-серый фон для четных строк
            else:
                option.backgroundBrush = QColor(255, 255, 255)  # Белый фон для нечетных строк
