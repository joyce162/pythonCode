import pymysql

from conf.oprationConfig import OprationConfig
from common.recordLog import log

config = OprationConfig()

class ConnectMysql(object):

    def __init__(self):
        conn_mysql={
            'host': config.get_option_from_database('host'),
            'port': int(config.get_option_from_database('port')),
            'username': config.get_option_from_database('username'),
            'password': config.get_option_from_database('password'),
            'database': config.get_option_from_database('database')
        }
        self.conn = pymysql.connect(**conn_mysql)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def query(self,sql):
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