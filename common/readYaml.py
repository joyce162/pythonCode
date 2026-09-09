import yaml
import os
from conf.setting import FILE_PATH


class ReadYaml(object):
    def __init__(self,filePath=None):
        if filePath is not None:
            self.filePath = filePath

    def get_testcase_from_yaml(self,file):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                testcase = yaml.safe_load(f)
                cases = testcase[0]['testcase']
                baseInfo = testcase[0]['baseInfo']

                if len(cases) >= 1:
                    result_list = []
                    for case in cases:
                        param = [baseInfo,case]
                        result_list.append(param)
                    return result_list
                else:
                    return testcase
        except Exception as e:
            print(e)

    def write_Yaml_data(self,writeValue):
        self.filePath = FILE_PATH['extract']
        if not os.path.exists(self.filePath):
            os.system(self.filePath)

        try:
            with open(self.filePath, 'a', encoding='utf-8') as f:
                if isinstance(writeValue,dict):
                    value = yaml.dump(writeValue,allow_unicode=True,sort_keys=False)
                    f.write(value)
        except Exception as e:
            print(e)

    def get_extract_data(self,nodeName):
        if os.path.exists(FILE_PATH['extract']):
            pass
        else:
            f = open(FILE_PATH['extract'], 'w', encoding='utf-8')
            f.close()
        with open(FILE_PATH['extract'], 'r', encoding='utf-8') as f:
            extract_data = yaml.safe_load(f)
            return extract_data[nodeName]

    def clear_extract_yml(self):
        with open(FILE_PATH['extract'], 'w', encoding='utf-8') as f:
            f.truncate()

if __name__ == '__main__':
    testcase = ReadYaml().get_testcase_from_yaml('../testcase/Login/loginTestcase.yml')
    # case = testcase[0]
    # url = "http://127.0.0.1:8787"+case['baseInfo']['url']
    # method = case['baseInfo']['method']
    # header = case['baseInfo']['header']
    # data = case['testcase'][0]['data']
    #
    # from common.sendRequests import SendRequests
    # sendRequests = SendRequests()
    # res = sendRequests.run_send(url,data,header,method)

    # writeValue = {}
    # writeValue['Token'] = res.json().get('token')
    #
    # ry = ReadYaml()
    # ry.write_Yaml_data(writeValue)

    # json_str = json.dumps(res.json(),ensure_ascii=False)
    # print(type(json_str))
    # js = json.loads(json_str)
    # print(type(js))