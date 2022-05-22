import sys

from PyQt5.QtWidgets import QApplication, QWidget

from model import WordSearchUI


if __name__ == '__main__':

    app = QApplication(sys.argv)
   
    win = WordSearchUI()
    win.show()

    sys.exit(app.exec_())

