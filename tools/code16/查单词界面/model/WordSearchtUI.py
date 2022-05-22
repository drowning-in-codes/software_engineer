from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QVBoxLayout, QMessageBox
)

from model.DictTable import TableWidget
from model import Window
from slot import GetWord, UpdateMean, DeleteWord
from constants import SearchConstants as sc


class WordSearchUI(Window):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):

        super().initUI()

        # 连接信号，绑定槽
        self.table.change_signal.connect(self.table_content_change)
        self.table.update_signal.connect(self.table_content_update)
        self.table.delete_signal.connect(self.table_content_delete)
        self.table.copy_signal.connect(self.table_content_copy)

    def right_layout(self):
        """右侧布局"""

        vbox = QVBoxLayout()

        self.table = TableWidget(count=GetWord.all_count(self.conn), data=GetWord.from_mysql(self.conn))
        self.table.setObjectName('widget')

        vbox.addWidget(self.table)

        return vbox

    def table_content_change(self, page):
        """表格翻页"""
        self.table.data = GetWord.from_mysql(self.conn, page=page)

    def table_content_update(self, means, word):
        """表格内容修改"""
        status = UpdateMean.update(self.conn, means=means, word=word)
        if not status:
            QMessageBox.warning(
                self, '警告', '修改错误',
                QMessageBox.No | QMessageBox.Yes,
                QMessageBox.Yes
            )
        else:
            self.statusBar().showMessage(sc.SEARCH_UPDATE_MESSAGE)

    def table_content_delete(self, word):
        """表格内容删除"""
        status = DeleteWord.delete(self.conn, word=word)
        if not status:
            QMessageBox.warning(
                self, '警告', '删除错误',
                QMessageBox.No | QMessageBox.Yes,
                QMessageBox.Yes
            )
        else:
            self.statusBar().showMessage(sc.SEARCH_DELETE_MESSAGE)

    def table_content_copy(self, text):
        """表格内容复制"""
        self.statusBar().showMessage(text + sc.SEARCH_COPY_MESSAGE)
