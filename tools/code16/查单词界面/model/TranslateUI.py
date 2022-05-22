import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QWidget, QApplication, QPushButton, QLineEdit,
    QTextEdit, QHBoxLayout, QVBoxLayout,
)

from TranslateAPI import Translate
from model import Window
from slot import CollectSlot, DictionarySlot
from QSSTool import QSSTool
from constants import TranslateConstants as tc


class TranslateUI(Window):

    collect_signal = pyqtSignal(str, str)
    dictionary_signal = pyqtSignal(str, str)

    bt = Translate()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.initUI()

    def initUI(self):
        super(TranslateUI, self).initUI()
        QSSTool.qss(self, tc.TRANSLATE_QSS_FILE_PATH)
        self.collect_signal.connect(self.collect_slot)
        self.dictionary_signal.connect(self.search_slot)
        self.show()

    def top_layout(self):
        """
            翻译界面右上侧布局
            return QHBoxLayout
        """

        hbox = QHBoxLayout()
        # setContentsMargins：设置盒子边距 参数：left,top,right,bottom
        hbox.setContentsMargins(0, 10, 0, 0)

        self.line = QLineEdit(self)
        self.line.setObjectName('line')
        self.line.setPlaceholderText(tc.TRANSLATE_PLACEHODERTEXT)

        clear_btn = QPushButton('清空', self.line)
        clear_btn.setGeometry(330, 0, 60, 45)
        # PointingHandCursor 当鼠标滑到按钮上时，鼠标显示成一个小手
        clear_btn.setCursor(Qt.PointingHandCursor)
        clear_btn.clicked.connect(self.clear)

        translate_btn = QPushButton(tc.TRANSLATE_BUTTON_NAME)
        translate_btn.setObjectName('translate')
        translate_btn.setCursor(Qt.PointingHandCursor)
        translate_btn.clicked.connect(self.translate)

        # 控件之间的空格间隙  设置伸展模式  这里为 6:1
        hbox.setSpacing(5)
        # 往布局中添加控件
        hbox.addWidget(self.line, stretch=6)
        hbox.addWidget(translate_btn, stretch=1)

        return hbox

    def right_layout(self):
        """
            翻译界面右侧布局
            return QVBoxLayout
        """

        vbox = QVBoxLayout()

        self.text_edit = QTextEdit()
        # 将文本编辑框设置成不聚焦模式
        self.text_edit.setFocusPolicy(Qt.NoFocus)

        vbox.setSpacing(10)
        vbox.addLayout(self.top_layout())
        vbox.addWidget(self.text_edit)

        return vbox

    def clear(self):
        """清空行编辑器（搜索框）中的内容"""

        self.line.clear()
        self.text_edit.clear()

    def translate(self):
        """
            翻译功能
            API 调用方式：
                >>> b = Translate()
                >>> b.translate("add a button")
                '添加按钮'
            也可以通过 BaiduTranslate.__doc__ 查看 API
        """

        text = self.line.text()
        result = self.bt.translate(text)

        if result:
            self.text_edit.setText(result)
            self.statusBar().showMessage(tc.TRANSLATE_success_MESSAGE)
            self.dictionary_signal.emit(text, result)
        else:
            self.statusBar().showMessage(tc.TRANSLATE_FAILURE_MESSAGE)

    def copy(self):
        """复制单词到剪切板"""

        clipboard = QApplication.clipboard()
        text = self.text_edit.toPlainText()

        if text:
            clipboard.setText(text)
            self.statusBar().showMessage(text + tc.TRANSLATE_COPY_MESSAGE)

    def collect(self):
        """收藏单词到单词本"""

        text = self.text_edit.toPlainText()

        if text:
            self.collect_signal.emit(self.line.text(), text)
            self.statusBar().showMessage(text + tc.TRANSLATE_COLLECT_MESSAGE)

    def collect_slot(self, word, means):
        CollectSlot.to_mysql(self.conn, word, means)

    def search_slot(self, word, means):
        DictionarySlot.to_mysql(self.conn, word, means)
