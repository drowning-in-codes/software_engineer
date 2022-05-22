# 本实验的图标地址为：https://labfile.oss.aliyuncs.com/courses/3841/calculator.jpg，请自行下载后上传至线上环境的 Code/calculator/images 目录
# 1.导包
import re
import sys

from PyQt5.QtWidgets import (
    QWidget, QApplication, QLineEdit, QPushButton,
    QLabel, QHBoxLayout, QVBoxLayout, QGridLayout,
    QDesktopWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from QSSTool.QSSTool import QSSTool


# 2.创建 Example 类
class Example(QWidget):

    # 11.初始化 调用 initUI 方法，展示窗口
    def __init__(self):
        super().__init__()
        self.setObjectName('widget')
        self.initUI()

    # 10.自定义 initUI 方法
    def initUI(self):
        # 添加布局
        self.setLayout(self.__layout())
        # 添加窗口图标
        self.setWindowIcon(QIcon('./images/calculator.jpg'))
        # 窗口居中
        self.center()
        self.setWindowTitle('计算器（PyQt5 项目实战）')
        self.show()

    # 3.窗口居中方法
    def center(self):
        """窗口居中"""

        # 获取窗口坐标
        qr = self.frameGeometry()
        # 获取屏幕中心点坐标
        cp = QDesktopWidget().availableGeometry().center()
        # 将窗口移动到屏幕中心点
        qr.moveCenter(cp)

    # 4.窗口整体布局
    def __layout(self):
        """
            窗口布局管理  ---> 垂直布局
            return LayoutObject
        """

        vbox = QVBoxLayout()

        hbox1 = self.top_widget()
        hbox2 = self.mid_widget()
        gbox = self.bottom_widget()

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(gbox)

        return vbox

    # 5.顶部布局 添加行编辑按钮 用来接受用户输入
    def top_widget(self):
        """
            Top Layout ---> 水平布局
            return QHBoxLayout
        """

        hbox = QHBoxLayout()

        self.line = QLineEdit()
        self.line.setAlignment(Qt.AlignRight)

        hbox.addWidget(self.line)

        return hbox

    # 6.中间布局 添加标签控件 用来显示计算结果
    def mid_widget(self):
        """
            Middle Layout ---> 水平布局
            return QHBoxLayout
        """

        hbox = QHBoxLayout()

        self.lable = QLabel()
        self.lable.setAlignment(Qt.AlignRight)

        hbox.addWidget(self.lable)

        return hbox

    # 7.底部布局 栅格布局添加按钮
    def bottom_widget(self):
        """
            Bottom Layout ---> 对按钮进行栅格布局
            return QGridLayout
        """

        gbox = QGridLayout()

        # 按钮名称、按钮在布局中的位置
        names = [
            '(', ')', 'x²', '√',
            'AC', '←', '+/-', '÷',
            '9', '8', '7', '×',
            '6', '5', '4', '-',
            '3', '2', '1', '+',
            '%', '0', '.', '='
        ]
        positions = [(i, j) for i in range(6) for j in range(4)]

        for name, position in zip(names, positions):
            b = QPushButton(name)
            # 添加点击事件
            b.clicked.connect(self.bclick)

            # 给按钮添加 ID 属性
            if position[0] == 0:
                b.setObjectName('row1')
            if position[1] == 3:
                b.setObjectName('col1')
            if position[0] == 5:
                b.setObjectName('row2')

            gbox.addWidget(b, *position)

        return gbox

    # 8.按钮点击事件
    def bclick(self):
        """
            按钮点击事件 ---> 回调函数
            处理按钮点击效果
        """

        text = self.sender().text()
        line_text = self.line.text()

        # 按下如下按钮，将进行字符串拼接
        if text in [
            '9', '8', '7', '6', '5', '4',
            '3', '2', '1', '0', '+', '-',
            '×', '÷', '(', ')', '.', '√',
            '%'
        ]:
            self.line.setText(line_text + text)

        # 按下 x² 按钮，平方 将进行字符串替换
        elif text == 'x²':
            self.line.setText(line_text+'^2')

        # 按下 AC 按钮，将进行字符串清空
        elif text == 'AC':
            self.line.setText('')
            self.lable.setText('')

        # 按下 ← 按钮，退格 删除一个字符
        elif text == '←':
            self.line.setText(line_text[:-1])

        # 按下 +/- 按钮，添加负数
        elif text == '+/-':
            x = re.findall("([\d]+)", line_text)
            if x:
                self.line.setText(line_text.rstrip(x[-1]) + '(-' + x[-1] + ')')
            else:
                self.line.setText('(-' + line_text + ')')

        # 按下  = 按钮，计算结果
        elif text == '=':
            self.calculate(line_text)

        # 仅仅使逻辑清晰，do nothing
        else:
            ...

    # 9.计算
    def calculate(self, line_text):
        """
            line_text：用户输入（行编辑控件中）的文本
            计算 在标签中显示结果
            将用户输入的文本进行处理，判断是否合法，并提炼成符合 python 语法的表达式进行计算
        """

        # 逻辑判断 检测、提炼、计算
        # 计算表达式是否为空
        if line_text == '':
            return

        # 计算表达式是否有乘法运算
        if '×' in line_text:
            line_text = line_text.replace('×', '*')

        # 计算表达式是否有除法运算
        if '÷' in line_text:
            line_text = line_text.replace('÷', '/')

        # 计算表达式是否有百分数运算
        if '%' in line_text:
            s = re.findall('([\.\d]+%)', line_text)
            if s:
                for i in s:
                    line_text = line_text.replace(i, str(eval(i[:-1] + '/100')))
            else:
                self.lable.setText('错误')
                return

        # 计算表达式是否有二次方根运算
        if '√' in line_text:
            s = re.findall('(√[\d]+)', line_text)
            if s:
                for i in s:
                    line_text = line_text.replace(i, i[1:] + '**0.5')
            else:
                self.lable.setText('错误')
                return

        # 计算表达式是否有平方运算
        if '^' in line_text:
            line_text = line_text.replace('^', '**')

        # 谨防不合法表达式
        try:
            self.lable.setText(str(eval(line_text)))
        except:
            self.lable.setText('错误')


# 12.实例化对象 主循环开始
if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    QSSTool.qss('./QSSTool/calculator.qss', app)
    sys.exit(app.exec_())
