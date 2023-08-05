import datetime
import pymysql
from dbutils.pooled_db import PooledDB


def singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton


@singleton
class MysqlManager(object):
    """docstring for DBManager"""

    def __init__(self, db_host, db_user, db_pass, db_name, db_port=3306, charset='utf8mb4'):
        self.db_host = db_host
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name
        self.db_port = db_port
        self.pool = PooledDB(
            creator=pymysql,
            mincached=2,
            maxcached=5,
            maxconnections=10,
            maxshared=3,
            blocking=True,
            maxusage=None,
            setsession=[],
            ping=0,
            host=self.db_host,
            user=self.db_user,
            passwd=self.db_pass,
            db=self.db_name,
            port=self.db_port,
            charset=charset)

    def execute(self, sql):
        db = self.pool.connection()
        try:
            db.cursor().execute(sql)
            db.commit()
            return db.cursor()
        except Exception as e:
            print("---rollback--{}".format(e))
            db.rollback()

    def select(self, sql):
        db = self.pool.connection()
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return None

