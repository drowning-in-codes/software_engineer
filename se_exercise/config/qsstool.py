class QSSTool:
    @staticmethod
    def qss(widget, file_path=None, file_path_list=None):
        """
            widget：控件
            file_path：QSS文件路径
            file_path_list：QSS文件路径列表
        """

        if file_path is not None:
            try:
                with open(file_path, encoding='utf-8') as f:
                    widget.setStyleSheet(f.read())
            except:
                print(file_path, "此文件不存在！")

        elif file_path_list is not None:
            for path in file_path_list:
                try:
                    with open(path, encoding='utf-8') as f:
                        widget.setStyleSheet(f.read())
                except:
                    print(path, "此文件不存在！")

        else:
            print("你没有输入QSS文件不存在！")