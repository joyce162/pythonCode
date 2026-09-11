import pymysql
from pymysql import cursors
import redis
from redis.cluster import RedisCluster

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
        :return:返回数据库查询结果，以dict形式
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
            raise
        finally:
            self.close()

class ConnectionRedis(object):
    def __init__(self):
        self.__conn_redis = {
            'host': config.get_option_from_redis('host'),
            'port': int(config.get_option_from_redis('port')),
            'user': config.get_option_from_redis('username'),
            'password': config.get_option_from_redis('password'),
            'db': config.get_option_from_redis('db')
        }
        self.startup_nodes_str = config.get_option_from_redis('startup_nodes')

        if self.startup_nodes_str:
            self.startup_node = []
            if self.startup_nodes_str:
                startup_nodes_list = self.startup_nodes_str.split(',')
                for node in startup_nodes_list:
                    host, port = node.split(':')
                    data = {"host": host, "port":port}
                    self.startup_node.append(data)
                # 多节点 startup_nodes=,多节点不能传db，默认db=0.不然会报错
                self.redis_cluster = RedisCluster(startup_nodes=self.startup_node,
                                                  user=self.__conn_redis['user'],
                                                  password=self.__conn_redis['password'],
                                                  decode_responses=True)
            else:
                # 单节点
                pool = redis.ConnectionPool(**self.__conn_redis)
                self.redis_cluster = redis.Redis(connection_pool=pool)

    def get(self,key):
        """
        从redis中获取数据
        :param key:redis key
        :return:redis 对应的value
        """
        try:
            return self.redis_cluster.get(key)
        except Exception as e:
            log.error(e)
            raise

    def set(self,key,value):
        """
        redis 设置
        :param key:
        :param value:
        """
        try:
            self.redis_cluster.set(key,value)
        except Exception as e:
            log.error(e)
            raise