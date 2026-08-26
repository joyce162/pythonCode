import json
from common.readYaml import ReadYaml
from common.debugTalk import DebugTalk


class BaseRequestUtil(object):
    def __init__(self):
        pass

    def replace_load(self,data):
        str_data = None
        if type(data) is not str:
            str_data = json.dumps(data,ensure_ascii=False)

        for i in range(str_data.count('${')):
            start_index = str_data.index('$')
            end_index = str_data.index('}',start_index)
            ref_all_params = str_data[start_index:end_index+1]
            print("ref_all_params:",ref_all_params)

            func_name = ref_all_params[2:ref_all_params.index('(')]
            print("func_name:", func_name)
            func_param = ref_all_params[ref_all_params.index('(')+1:ref_all_params.index(')')]
            print("func_param:", func_param)
            print(type(func_param))

            extra_data = getattr(DebugTalk(),func_name)(*func_param.split(',') if func_param else [])
            print("extra_data:", extra_data)

            print("replace前：",str_data)
            str_data = str_data.replace(ref_all_params,extra_data)
            print("replace后：", str_data)

        #还原数据
        if data and isinstance(data,dict):
            data = json.loads(str_data)
        else:
            data = str_data
        return data

if __name__ == '__main__':
    ry = ReadYaml()
    testcase = ry.get_testcase_from_yaml('loginTestcae.yml')

    base = BaseRequestUtil()
    base.replace_load(testcase)
