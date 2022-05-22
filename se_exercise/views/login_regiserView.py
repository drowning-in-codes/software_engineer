import os

from PyQt5.QtWidgets import QWidget, QLabel, QMainWindow, QCheckBox, QPushButton, QDesktopWidget, QLineEdit, \
    QVBoxLayout, QHBoxLayout, QFormLayout
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QMouseEvent
from config import LC
from config import QSSTool


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.picLabel = None
        self.initUI()

    def initUI(self):
        # 初始化窗口 配置基本项

        # self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlag(Qt.FramelessWindowHint)  # 无边框
        self.setWindowTitle(LC.FORM_TITLE)

        # self.

        # 配置qss
        # QSSTool.qss()
        self.center()
        self.__layout()

    def center(self):
        """窗口居中"""
        self.resize(LC.FORM_WIDTH, LC.FORM_HEIGHT)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) / 2,
            (screen.height() - size.height()) / 2
        )

    def __layout(self):
        mainwidget = QWidget()
        # 设置窗体名字
        mainwidget.setObjectName("MainWidget")

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        picLabel = self.left_layout()
        picLabel.setObjectName("imgLabel")
        vbox.addWidget(picLabel)
        hbox.addLayout(vbox)

        hbox.addLayout(self.right_layout())

        # 对半分
        hbox.setStretch(0, 1)
        hbox.setStretch(1, 1)

        # CentralWidget设置水平布局
        mainwidget.setLayout(hbox)
        self.setCentralWidget(mainwidget)

    def left_layout(self):
        picLabel = QLabel(self)
        picLabel.setStyleSheet("border-image:url('./resource/img/登录图.jpg');\n")
        return picLabel

    def right_layout(self):
        layout = QVBoxLayout(self)
        accountLine = QLineEdit()
        accountLine.setPlaceholderText("输入账号")
        passwordLine = QLineEdit()
        passwordLine.setPlaceholderText("输入密码")
        passwordLine.setEchoMode(QLineEdit.Password)
        confirmButton = QPushButton("确定")
        layout.addWidget(accountLine)
        layout.addWidget(passwordLine)

        layout.addWidget(confirmButton)
        layout.addWidget(QCheckBox("忘记密码?", self))


        return layout

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None
