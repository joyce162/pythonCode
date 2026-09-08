import random

from common.readYaml import ReadYaml
class DebugTalk(object):
    def __init__(self):
        self.read = ReadYaml()

    def get_extract_data(self,nodeName, secondNode=None):
        """
        该方法处理的数据为：{"token":"123456"}或{"auth":{"token":"123456"}}
        :param nodeName: 第一个的token，第二个的auto
        :param secondNode: 第一个none，第二个token
        :return:
        """
        data = self.read.get_extract_data(nodeName)

        if secondNode == None:
            return data
        else:
            return data[secondNode]

    def get_extract_data_list(self,nodeName,randoms=None):
        """
        该方法处理的数据为：{"token":['123456','123456','123456','']}
        :param nodeName:
        :param randoms: 0：在列表中取任意值，-1：将列表合并为str，-2：取整个列表
        :return:
        """
        data = self.read.get_extract_data(nodeName)

        if randoms is None:
            return data
        else:
            ran = int(randoms)
            dataValue = {
                0: random.choice(data),
                -1: ','.join(data),
                -2: ','.join(data).split(',')
            }
            return dataValue[ran]

    def get_extract_order_data(self,nodeName,orderIndex):
        """
        该方法处理的数据为：{"token":['123456','123456','123456','']}
        :param nodeName:
        :param orderIndex: 列表索引
        :return:
        """
        data = self.read.get_extract_data(nodeName)
        value = data[nodeName]
        return value[orderIndex]

if __name__ == '__main__':
    debug = DebugTalk()
    debug.get_extract_data('ProductId',-1)