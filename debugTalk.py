import random

from readYaml import ReadYaml
class DebugTalk:
    def __init__(self):
        self.read = ReadYaml()

    def get_extract_data(self,nodeName,randoms=None):
        data = self.read.get_extract_data(nodeName)
        print(data)
        print(type(data))
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

if __name__ == '__main__':
    debug = DebugTalk()
    debug.get_extract_data('ProductId',-1)