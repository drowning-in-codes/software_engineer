from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit,
    QHBoxLayout, QVBoxLayout, QHeaderView, QTableWidget,
    QLabel, QMessageBox, QButtonGroup, QAbstractItemView,
    QTableView, QTableWidgetItem, QInputDialog
)
from PyQt5.QtCore import Qt

from QSSTool import QSSTool
from constants import TableConstants as tc


class TableWidget(QWidget):

    change_signal = pyqtSignal(str)
    update_signal = pyqtSignal(str, str)
    delete_signal = pyqtSignal(str)
    copy_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):

        # API: count：数据库中的总条数 data：8条初始数据
        if kwargs.get('count') is not None:
            count = kwargs.pop('count')
        else:
            count = 0
        if kwargs.get('data') is not None:
            self.data = kwargs.pop('data')
        else:
            self.data = ()
        if count and count % tc.TABLE_DATA_SHOW_COUNT == 0:
            self.page = count // tc.TABLE_DATA_SHOW_COUNT
        else:
            self.page = count // tc.TABLE_DATA_SHOW_COUNT + 1

        super(TableWidget, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):

        self.setLayout(self.__layout())
        QSSTool.qss(self, tc.TABLE_QSS_FILE_PATH)

    def __layout(self):
        """
            表格布局 和 Window.py 的 __layout 方法不一样，
            注意区别，这里是自定义表格控件的布局方法
        """

        vbox = QVBoxLayout()

        # 8行3列的表格
        self.table = QTableWidget(tc.TABLE_DEFAULT_ROW, tc.TABLE_DEFAULT_COLUMN)
        # 表头
        self.table.setHorizontalHeaderLabels(tc.TABLE_HEADER_LIST)
        # 所有列自动拉伸，充满界面
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 表头高度
        self.table.horizontalHeader().setFixedHeight(tc.TABLE_HEADER_HEIGHT)
        # 设置只能选中一行
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        # 不可编辑
        self.table.setEditTriggers(QTableView.NoEditTriggers)
        # 设置只有行选中，不能多选
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        for i in range(tc.TABLE_DEFAULT_ROW):
            # 设置行高
            self.table.setRowHeight(i, tc.TABLE_ROW_HEIGHT)

        self.data_show()

        vbox.addWidget(self.table)
        vbox.addLayout(self.page_layout())

        return vbox

    def page_layout(self):
        """页码布局"""

        hbox = QHBoxLayout()
        hbox.setSpacing(0)

        home_page = QPushButton("首页")
        last_page = QPushButton("<上一页")
        page1 = QPushButton("1")
        page2 = QPushButton("2")
        page3 = QPushButton("3")
        page4 = QPushButton("4")
        page5 = QPushButton("5")
        next_page = QPushButton("下一页>")
        finally_page = QPushButton("尾页")
        self.total_page = QLabel("共" + str(self.page) + "页")
        skip_to = QLabel("跳到")
        self.skip_page = QLineEdit()
        skip_page_to = QLabel("页")
        confirm = QPushButton("确定")

        # 创建按钮组
        self.group = QButtonGroup(self)
        btn_list = [page1, page2, page3, page4, page5]
        for b in btn_list:
            self.group.addButton(b)
            b.setCheckable(True)
            b.clicked.connect(self.changeTableContent)
        self.group.buttons()[0].setChecked(True)

        # 给按钮设置小手
        btn_list += [
            home_page, last_page, finally_page,
            next_page, skip_to, confirm
        ]
        for b in btn_list:
            b.setCursor(Qt.PointingHandCursor)

        # 将控件添加到布局中
        w_list = [
            home_page, last_page, page1, page2,
            page3, page4, page5, next_page,
            finally_page, self.total_page, skip_to, self.skip_page,
            skip_page_to, confirm
        ]
        objectname_list = [
            'home_page', 'last_page', 'page1', 'page2',
            'page3', 'page4', 'page5', 'next_page',
            'finally_page', 'total_page', 'skip_to', 'skip_page',
            'skip_page_to', 'confirm'
        ]

        for w, objectname in zip(w_list, objectname_list):
            w.setObjectName(objectname)
            hbox.addWidget(w)

        # 连接槽函数
        home_page.clicked.connect(self.__home_page)
        last_page.clicked.connect(self.__last_page)
        next_page.clicked.connect(self.__next_page)
        finally_page.clicked.connect(self.__finally_page)
        confirm.clicked.connect(self.__confirm_skip)

        return hbox

    def __home_page(self):
        """点击首页信号"""

        buttons = self.group.buttons()

        for i in range(5):
            buttons[i].setText(str(i+1))
        buttons[0].setChecked(True)

        self.changeTableContent()

    def __last_page(self):
        """点击上一页信号"""

        # 获取页码和当前页按钮位置
        buttons = self.group.buttons()
        for b in buttons:
            if b.isChecked():
                page = b.text()
                index = buttons.index(b)
                break

        if page == '1':
            QMessageBox.information(self, "提示", "已经是第一页了", QMessageBox.Yes)
            return

        # 如果是第一个按钮被选中则页码减一，否则前一个按钮被选中
        if index == 0:
            p = range(int(page) - 1, int(page) + 4)

            for i in range(5):
                buttons[i].setText(str(p[i]))
            buttons[index].setChecked(True)
        else:
            buttons[index-1].setChecked(True)

        self.changeTableContent()

    def __next_page(self):
        """点击下一页信号"""

        total_page = self.total_page.text()[1:-1]
        buttons = self.group.buttons()

        for b in buttons:
            if b.isChecked():
                page = b.text()
                index = buttons.index(b)
                break

        if page == total_page:
            QMessageBox.information(self, "提示", "已经是最后一页了", QMessageBox.Yes)
            return

        if index == 4 and int(total_page) > 5:
            p = range(int(page) - 3, int(page) + 2)
            for i in range(5):
                buttons[i].setText(str(p[i]))
            buttons[index].setChecked(True)
        else:
            buttons[index + 1].setChecked(True)

        self.changeTableContent()

    def __finally_page(self):
        """点击尾页信号"""
        total_page = self.total_page.text()[1:-1]
        buttons = self.group.buttons()

        if int(total_page) <= 5:
            p = range(1, 6)
        else:
            p = range(int(total_page) - 4, int(total_page) + 1)
        for i in range(5):
            buttons[i].setText(str(p[i]))
        buttons[-1].setChecked(True)

        self.changeTableContent()

    def __confirm_skip(self):
        """页码跳转信号"""
        total_page = self.total_page.text()[1:-1]
        buttons = self.group.buttons()

        page = self.skip_page.text()

        if not page:
            return

        self.skip_page.clear()

        if int(total_page) < int(page) or int(page) < 0:
            QMessageBox.information(self, "提示", "跳转页码超出范围", QMessageBox.Yes)
            return

        if int(page) + 5 > int(total_page):
            p = range(int(total_page) - 4, int(total_page) + 1)
            for i in range(5):
                buttons[i].setText(str(p[i]))
                if p[i] == int(page):
                    buttons[i].setChecked(True)
        else:
            p = range(int(page), int(page) + 5)
            for i in range(5):
                buttons[i].setText(str(p[i]))
                if str(p[i]) == page:
                    buttons[0].setChecked(True)

        self.changeTableContent()

    def data_show(self):
        """每页的数据展示"""

        self.table.clearContents()

        for r in range(8):

            if r >= len(self.data):
                break

            word, means = self.data[r]

            word_item = QTableWidgetItem(word)
            means_item = QTableWidgetItem(means)

            word_item.setTextAlignment(Qt.AlignCenter)
            means_item.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(r, 0, QTableWidgetItem(word_item))
            self.table.setItem(r, 1, QTableWidgetItem(means_item))
            self.table.setCellWidget(r, 2, self.oparate(r))

    def oparate(self, row):
        """设置操作按钮"""

        w = QWidget()

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)

        btn_name_list = ['删除', '修改', '复制']
        btn_objectname_list = ['delete', 'update', 'copy']
        btn_click_event_list = [self.__delete, self.__update, self.__copy]

        for btn_name, btn_objectname, btn_click_event in zip(
                btn_name_list, btn_objectname_list, btn_click_event_list):

            btn = QPushButton(btn_name)
            btn.setObjectName(btn_objectname)
            btn.clicked.connect(btn_click_event)
            btn.setMinimumSize(50, 39)
            btn.setCursor(Qt.PointingHandCursor)
            btn.row = row

            hbox.addWidget(btn)

        w.setLayout(hbox)

        return w

    def __delete(self):
        """删除操作按钮点击事件"""

        row = self.sender().row
        word = self.table.item(row, 0).text()
        self.delete_signal.emit(word)
        self.changeTableContent()

    def __update(self):
        """修改操作按钮点击事件"""

        row = self.sender().row
        word = self.table.item(row, 0).text()
        text, sure = QInputDialog.getText(self, "修改", "请输入修改内容：", QLineEdit.Normal, "")
        if sure and text:
            self.update_signal.emit(text, word)
        self.changeTableContent()

    def __copy(self):
        """复制操作按钮点击事件"""

        row = self.sender().row
        clipboard = QApplication.clipboard()

        word = self.table.item(row, 0).text()
        means = self.table.item(row, 1).text()
        text = word + ':' + means

        clipboard.setText(text)
        self.copy_signal.emit(text)

    def changeTableContent(self):
        """发射当前页表格内容改变信号"""
        btn = self.group.checkedButton()
        self.change_signal.emit(btn.text())

        self.data_show()
