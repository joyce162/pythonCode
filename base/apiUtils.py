import json
from common.readYaml import ReadYaml
from common.debugTalk import DebugTalk
from conf.oprationConfig import OprationConfig
from common.sendRequests import SendRequests


class BaseRequestUtil(object):
    def __init__(self):
        self.ry = ReadYaml()
        self.dt = DebugTalk()
        self.oc = OprationConfig()
        self.sr = SendRequests()


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

    def specification_yaml(self,case_info):
        host = self.oc.get_option_from_env('host')
        url = host + case_info['baseInfo']['url']
        method = case_info['baseInfo']['method']
        api_name = case_info['baseInfo']['api_name']
        headers = case_info['baseInfo']['header']
        cookie = case_info['baseInfo']['cookie']
        testcase = case_info['testcase']

        cookie = None
        if case_info['baseInfo'].get('cookie'):
            cookie = self.replace_load(case_info['baseInfo'].get('cookie'))


        for tc in testcase:
            tc.pop('validation')
            tc.pop('extract')
            tc.pop('case_name')
            res = self.sr.run_main(
                case_name=api_name,
                url=url,
                method=method,
                headers=headers,
                cookie=cookie,
                **tc)
            # for key,value in tc.items():
            #     if key in request_body_type:
            #         if key == 'data':
            #             res = self.sr.run_send(url=url,data=value,headers=headers,method=method)
            #             print(res.json())





if __name__ == '__main__':
    testcase = ReadYaml().get_testcase_from_yaml('../testcase/Login/loginTestcase.yml')
    print(testcase[0])
    base = BaseRequestUtil()
    base.specification_yaml(testcase[0])

    # base = BaseRequestUtil()
    # base.replace_load(testcase)

