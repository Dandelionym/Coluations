import pymysql

db = 'sobot'


class SqlHelper(object):
    def __init__(self):
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host='222.19.236.134', port=3306, user='root',
                                    passwd='Bot_123456', use_unicode=True, db=db, charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_list(self, sql: object, args: object) -> object:
        """

        :rtype:
        """
        self.cursor.execute(sql, args)
        return self.cursor.fetchall()

    def get_one(self, sql: object, args: object) -> object:
        self.cursor.execute(sql, args)
        return self.cursor.fetchone()

    def modify(self, sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()

    def multipleModify(self, sql, args):
        self.cursor.executemany(sql, args)
        self.conn.commit()

    def create(self, sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.conn.close()

