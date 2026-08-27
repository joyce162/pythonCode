import configparser
from conf.setting import FILE_PATH

class oprationConfig:
    def __init__(self, filePath=None):
        if filePath is None:
            self.__filePath = FILE_PATH['conf']
        else:
            self.__filePath = filePath
        self.config = configparser.ConfigParser()
        try:
            self.config.read(self.__filePath,encoding='utf-8')
        except Exception as e:
            print(e)

    def get_section_for_data(self,section,option):
        data = self.config.get(section,option)
        return data

