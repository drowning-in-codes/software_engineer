# 2.编写 QSS 工具类
class QSSTool:
    @staticmethod
    def qss(file_path, widget):
        with open(file_path) as f:
            widget.setStyleSheet(f.read())
