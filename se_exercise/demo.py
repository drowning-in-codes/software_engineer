import sys
from PyQt5 import QtWidgets
from qt_material import apply_stylesheet
from myui import Ui_MainWindow

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

# setup stylesheet
apply_stylesheet(app, theme='dark_teal.xml')

# run
window.show()
app.exec_()
