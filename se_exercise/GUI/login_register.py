# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 628)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 69, 320, 441))
        self.label.setStyleSheet("border-image: url(:/img/登录图.jpg);\n"
"border-top-left-radius:50px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")




        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 69, 371, 441))
        self.label_2.setStyleSheet("border-bottom-right-radius:40px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(440, 130, 211, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton {\n"
"border:none;\n"
"}\n"
"\n"
"#pushButton:focus {\n"
"    color: rgb(255, 140, 74);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2 {\n"
"border:none;\n"
"}\n"
"\n"
"#pushButton_2:focus {\n"
"    color: rgb(255, 140, 74);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(410, 200, 301, 291))
        self.widget_2.setObjectName("widget_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 1px solid rgb(0, 0, 0);\n"
"border-radius:8px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 100, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border: 1px solid rgb(0, 0, 0);\n"
"border-radius:8px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 220, 261, 61))
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:16px;    \n"
"    background-color: rgb(0, 0, 0);\n"
"    border:6px solid black;\n"
"}\n"
"\n"
"#pushButton_3:hover{\n"
"    color: rgb(0,0,0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#pushButton_3:pressed{\n"
"    padding-left:6px;\n"
"    padding-top:6px;\n"
"}\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox.setGeometry(QtCore.QRect(30, 190, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 80, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border:none;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(410, 200, 301, 291))
        self.widget_3.setObjectName("widget_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 20, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border: 1px solid rgb(0, 0, 0);\n"
"border-radius:8px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 90, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border: 1px solid rgb(0, 0, 0);\n"
"border-radius:8px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 160, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border: 1px solid rgb(0, 0, 0);\n"
"border-radius:8px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 220, 261, 61))
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:16px;    \n"
"    background-color: rgb(0, 0, 0);\n"
"    border:6px solid black;\n"
"}\n"
"\n"
"#pushButton_5:hover{\n"
"    color: rgb(0,0,0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#pushButton_5:pressed{\n"
"    padding-left:6px;\n"
"    padding-top:6px;\n"
"}\n"
"\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton_4.raise_()
        self.widget_3.raise_()
        self.widget_2.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setText(_translate("MainWindow", "注册"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "输入账号"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "输入密码"))
        self.pushButton_3.setText(_translate("MainWindow", "登录"))
        self.checkBox.setText(_translate("MainWindow", "记住密码"))
        self.pushButton_4.setText(_translate("MainWindow", "X"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "输入账号"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "输入密码"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "确认密码"))
        self.pushButton_5.setText(_translate("MainWindow", "注册"))
