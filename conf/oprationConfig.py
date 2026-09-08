import configparser
from conf.setting import FILE_PATH

class OprationConfig:
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

    def get_option_from_env(self,option):
        return self.get_section_for_data('API_ENV',option)

    def get_option_from_database(self,option):
        return self.get_section_for_data('MYSQL',option)
