import pymysql
from pymysql import cursors

from conf.oprationConfig import OprationConfig
from common.recordLog import log

config = OprationConfig()

class ConnectMysql(object):

    def __init__(self):
        self.__conn_mysql={
            'host': config.get_option_from_database('host'),
            'port': int(config.get_option_from_database('port')),
            'user': config.get_option_from_database('username'),
            'password': config.get_option_from_database('password'),
            'database': config.get_option_from_database('database')
        }
        self.conn = pymysql.connect(**self.__conn_mysql)
        self.cursor = self.conn.cursor(cursor=cursors.DictCursor)

    def close(self):
        self.cursor.close()
        self.conn.close()

    def query(self,sql):
        """
        查询数据库操作
        :param sql:查询sql语句
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            res = self.cursor.fetchall()
            return res
        except Exception as e:
            log.error(e)
        finally:
            if self.cursor and self.conn:
                self.close()

    def excuteSql(self,sql):
        """
        执行增删改
        :param sql:增删改sql语句
        :return:
        """
        try:
            rows = self.cursor.execute(sql)
            self.conn.commit()
            return rows
        except Exception as e:
            log.error(e)
            # 如遇失败数据回滚
            self.conn.rollback()
        finally:
            self.close()