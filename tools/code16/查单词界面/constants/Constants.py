import os

WORK_PATH = os.getcwd()


class WindowConstants:

    WINDOW_WORK_PATH = WORK_PATH
    WINDOW_QSS_FILE_PATH = WORK_PATH + '/QSSTool/window.qss'
    WINDOW_ICON_PATH = WORK_PATH + '/resource/images/translate.png'

    WINDOW_WELCOM_MESSAGE = "欢迎来到蓝桥云课学习 PyQt5!"
    WINDOW_TITLE = '单词神器'

    WINDOW_WIDTH = 680
    WINDOW_HEIGHT = 400


class TranslateConstants:

    TRANSLATE_QSS_FILE_PATH = WORK_PATH + '/QSSTool/translate.qss'
    TRANSLATE_PLACEHODERTEXT = '请输入翻译的词语或语句'

    TRANSLATE_BUTTON_NAME = "翻译一下"

    TRANSLATE_success_MESSAGE = '翻译成功！'
    TRANSLATE_FAILURE_MESSAGE = '翻译失败！'
    TRANSLATE_COPY_MESSAGE = " 已复制到剪切板！"
    TRANSLATE_COLLECT_MESSAGE = " 已收藏至单词本！"


class SearchConstants:

    SEARCH_UPDATE_MESSAGE = '单词意思修改成功！'
    SEARCH_DELETE_MESSAGE = '删除成功！'
    SEARCH_COPY_MESSAGE = " 已复制到剪切板！"


class TranslateFileConstants:

    TRANSLATEFILE_QSS_FILE_PATH = WORK_PATH + '/QSSTool/translatefile.qss'
    TRANSLATEFILE_FILE_PATH = WORK_PATH + '/resource/将进酒.txt'


class TableConstants:

    TABLE_QSS_FILE_PATH = WORK_PATH + '/QSSTool/dicttable.qss'

    TABLE_DEFAULT_ROW = TABLE_DATA_SHOW_COUNT = 8
    TABLE_DEFAULT_COLUMN = 3

    TABLE_HEADER_LIST = ['单词', '意思', '操作']

    TABLE_HEADER_HEIGHT = 29
    TABLE_ROW_HEIGHT = 39
