import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint, Qt

from model import Login_Window
from qt_material import apply_stylesheet
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMouseEvent


class MyWindow(QMainWindow, Login_Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlag(Qt.FramelessWindowHint)  # 无边框

        self.pushButton.clicked.connect(self.change_widget2)
        self.pushButton_2.clicked.connect(self.change_widget3)
        self.widget_3.hide()

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

    def change_widget3(self):
        self.widget_2.hide()
        self.widget_3.show()

    def change_widget2(self):
        self.widget_3.hide()
        self.widget_2.show()


# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
# setup stylesheet
# apply_stylesheet(app, theme='dark_teal.xml')
# run
sys.exit(app.exec())
