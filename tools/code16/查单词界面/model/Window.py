import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QPushButton,
    QDesktopWidget, QHBoxLayout, QVBoxLayout, QAction,
    QButtonGroup, qApp
)

from QSSTool.QSSTool import QSSTool
from constants import WindowConstants as wc
from database import DataBase


class Window(QMainWindow):
    """
        所有窗口的基类，定义了左侧窗口布局，设计了公用的信号机制和布局接口，以及菜单样式
    """

    # 页面切换信号
    word_translate_page_signal = pyqtSignal()
    search_page_signal = pyqtSignal()
    recite_page_signal = pyqtSignal()
    file_translate_page_signal = pyqtSignal()

    conn = DataBase.connect()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    def initUI(self):

        self.statusBar().showMessage(wc.WINDOW_WELCOM_MESSAGE)

        self.center()
        QSSTool.qss(self, wc.WINDOW_QSS_FILE_PATH)
        self.setWindowTitle(wc.WINDOW_TITLE)
        self.setWindowIcon(QIcon(wc.WINDOW_ICON_PATH))
        
        self.__layout()

    def center(self):
        """窗口居中"""
        
        self.resize(wc.WINDOW_WIDTH, wc.WINDOW_HEIGHT)

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        
        self.move(
            (screen.width() - size.width()) / 2,
            (screen.height() - size.height()) / 2
        )

    def left_layout(self):
        """
            左侧导航布局
            return QVBoxLayout
        """

        btn_name_list = ['翻译', '查词典', '背单词', '译文档', '复制', '收藏']
        btn_click_event_list = [
            self.__translate_word_page, self.__search_word_page, self.__recite_word_page,
            self.__translate_file_page, self.copy, self.collect,
        ]

        vbox = QVBoxLayout()
        self.g = QButtonGroup()

        for name, btn_click_event in zip(btn_name_list, btn_click_event_list):
            b = QPushButton(name)
            b.setCursor(Qt.PointingHandCursor)
            b.setObjectName('left_btn')
            b.setCheckable(True)
            b.clicked.connect(btn_click_event)

            self.g.addButton(b)
            vbox.addWidget(b)

        self.g.buttons()[0].setChecked(True)

        return vbox

    def right_layout(self):
        """
            右侧布局，供各个窗口重写此方法自定义右侧布局
            return QVBoxLayout
        """

        vbox = QVBoxLayout()
        return vbox

    def __layout(self):
        """窗口整体布局"""

        widget = QWidget()
        # 由于 QMainWindow 中设计了自己的一套布局，贸然添加盒子布局会打破原有的自身的布局，
        # 所以把控件的父类替换成 QWidget，QWidget 将作为所有基础控件的父类
        self.setCentralWidget(widget)

        hbox = QHBoxLayout()

        vbox_left = self.left_layout()
        vbox_right = self.right_layout()

        hbox.addLayout(vbox_left)
        hbox.addLayout(vbox_right)

        # 左侧布局占据窗口空间的七分之一，右侧布局占据窗口空间的七分之六
        hbox.setStretch(1, 1)
        hbox.setStretch(2, 6)

        widget.setLayout(hbox)

    def __translate_word_page(self):
        """单词翻译页面信号发射"""
        self.word_translate_page_signal.emit()

    def __search_word_page(self):
        """查单词"页面信号发射"""
        self.search_page_signal.emit()

    def __recite_word_page(self):
        """背单词页面信号发射"""
        self.recite_page_signal.emit()

    def __translate_file_page(self):
        """文档翻译页面信号发射"""
        self.file_translate_page_signal.emit()

    def copy(self):
        """单词复制接口，在翻译页面重写"""
        ...

    def collect(self):
        """单词收藏接口，在翻译页面重写"""
        ...

