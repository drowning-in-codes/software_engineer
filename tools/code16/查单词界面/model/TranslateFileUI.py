import sys

from PyQt5.QtWidgets import (
    QPushButton, QTextEdit, QFileDialog, QLabel,
    QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import QDir, Qt

from model import Window
from TranslateAPI import Translate
from QSSTool import QSSTool
from constants import TranslateFileConstants as tfc


class TranslateFileUI(Window):

    bt = Translate()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        super(TranslateFileUI, self).initUI()
        QSSTool.qss(self, tfc.TRANSLATEFILE_QSS_FILE_PATH)

    def top_layout(self):
        """上部布局"""

        hbox = QHBoxLayout()
        hbox.setSpacing(20)
        hbox.setContentsMargins(12, 10, 15, 0)

        # 创建按钮
        file_btn = QPushButton('加载文档')
        clear_btn = QPushButton('清空')
        translate_btn = QPushButton('翻译')

        # 设置手型
        file_btn.setCursor(Qt.PointingHandCursor)
        clear_btn.setCursor(Qt.PointingHandCursor)
        translate_btn.setCursor(Qt.PointingHandCursor)

        # 设置 objectname
        file_btn.setObjectName('file_btn')
        clear_btn.setObjectName('clear_btn')
        translate_btn.setObjectName('translate_btn')

        # 绑定点击事件
        file_btn.clicked.connect(self.loadText)
        clear_btn.clicked.connect(self.__clear_text)
        translate_btn.clicked.connect(self.translate_file)

        hbox.addWidget(file_btn)
        hbox.addWidget(clear_btn)
        hbox.addWidget(translate_btn)

        return hbox

    def right_layout(self):
        """右侧整体布局"""

        vbox = QVBoxLayout()
        vbox.setContentsMargins(5, 10, 15, 0)

        self.text_edit = QTextEdit()
        self.result_widget = QTextEdit()

        self.text_edit.setObjectName('text_edit')
        self.result_widget.setObjectName('result_widget')
        self.result_widget.setCursor(Qt.PointingHandCursor)

        # 右侧布局上中下三部分所占空间比为 1:4:4
        vbox.addLayout(self.top_layout(), stretch=1)
        vbox.addWidget(self.text_edit, stretch=4)
        vbox.addWidget(self.result_widget, stretch=4)

        return vbox

    def loadText(self):
        """加载文档"""

        dialog = QFileDialog()
        # 获取选中文件绝对路径
        file_path = dialog.getOpenFileName(self, "选取文件", tfc.TRANSLATEFILE_FILE_PATH, "Text Files(*.txt)")[0]

        if file_path:
            with open(file_path, encoding='utf-8') as f:
                data = f.read()
                self.text_edit.setText(data)

    def translate_file(self):
        """翻译文档"""

        text = self.text_edit.toPlainText()

        if not text:
            self.statusBar().showMessage('翻译内容为空！')
        else:
            result_list = [[j for j in i.split('。') if j] for i in text.split('\n')]
            result = ''
            for x in result_list:
                y = [self.bt.translate(i) for i in x]
                result += ''.join(y) + '\n'
                self.result_widget.setText(result)
                
    def __clear_text(self):
        """清空控件内容"""

        self.text_edit.clear()
        self.result_widget.clear()
