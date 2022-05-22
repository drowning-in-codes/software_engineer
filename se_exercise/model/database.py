class DataBase:
    """数据库"""

    @staticmethod
    def connect(
            host='localhost', user='root',
            password='123456', db='translate'
    ):
        db_config = {
            'host': host,
            'port': 3306,
            'user': user,
            # 'password': password,
            'db': db,
            'charset': 'utf8',
        }

        import pymysql
        try:
            return pymysql.connect(**db_config)
        except:
            raise pymysql.err.MySQLError
