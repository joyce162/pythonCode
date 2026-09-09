import json
import re
import allure
import jsonpath

from common.readYaml import ReadYaml
from common.debugTalk import DebugTalk
from conf.oprationConfig import OprationConfig
from common.sendRequests import SendRequests
from common.recordLog import log
from common.assertions import Assertions


class BaseRequestUtil(object):
    def __init__(self):
        self.ry = ReadYaml()
        self.dt = DebugTalk()
        self.oc = OprationConfig()
        self.sr = SendRequests()
        self.ass = Assertions()

    def replace_load(self, data):
        str_data = data
        if not isinstance(data, str):
            str_data = json.dumps(data, ensure_ascii=False)

        for i in range(str_data.count('${')):
            start_index = str_data.index('$')
            end_index = str_data.index('}', start_index)
            ref_all_params = str_data[start_index:end_index + 1]
            log.info("ref_all_params: %s" % ref_all_params)

            func_name = ref_all_params[2:ref_all_params.index('(')]
            func_param = ref_all_params[ref_all_params.index('(') + 1:ref_all_params.index(')')]
            log.info("func_param: %s" % str(func_param))

            extra_data = getattr(DebugTalk(), func_name)(*func_param.split(',') if func_param else [])
            log.info("extra_data: %s" % extra_data)

            log.info("replace前：%s" % str_data)
            str_data = str_data.replace(ref_all_params, str(extra_data))
            log.info("replace后：%s" % str_data)

        # 还原数据
        if data and isinstance(data, dict):
            data = json.loads(str_data)
        else:
            data = str_data
        return data

    def specification_yaml(self, baseInfo, testcase):

        # 添加异常，不然非调用接口报错不会提示fail
        try:
            host = self.oc.get_option_from_env('host')
            url = host + baseInfo['url']
            allure.attach(url, f'接口地址: {url}', allure.attachment_type.TEXT)
            method = baseInfo['method']
            allure.attach(method, f'方法: {method}', allure.attachment_type.TEXT)
            api_name = baseInfo['api_name']
            allure.attach(api_name, f'接口名称: {api_name}', allure.attachment_type.TEXT)
            headers = baseInfo['header']
            allure.attach(str(headers), f'接口请求头: {headers}', allure.attachment_type.TEXT)

            # cookie 处理
            cookie = None
            try:
                if baseInfo['cookie']:
                    cookie = eval(self.replace_load(baseInfo['cookie']))
                    log.info(f'cookie: {cookie}')
                    allure.attach(cookie, f'cookie: {cookie}', allure.attachment_type.TEXT)
            except Exception:
                pass

            log.info(f'testcase:{testcase}')
            validation = testcase.pop('validation')
            extract = testcase.pop('extract', None)
            extract_list = testcase.pop('extract_list', None)
            case_name = testcase.pop('case_name')
            allure.attach(case_name, f'用例名称: {case_name}', allure.attachment_type.TEXT)

            for key, value in testcase.items():
                testcase[key] = self.replace_load(value)

            res = self.sr.run_main(
                case_name=case_name,
                url=url,
                method=method,
                headers=headers,
                cookies=cookie,
                **testcase)
            res_txt = res.text
            allure.attach(res_txt, f'接口响应: {res_txt}', allure.attachment_type.TEXT)



            if extract != None and extract != 'None':
                self.extract_data(extract, res_txt)
            if extract_list != None and extract_list != 'None':
                self.extract_data_list(extract_list, res_txt)

            if validation:
                self.ass.assert_result(validation, res.json(), res.status_code)

        except Exception as e:
            log.error(e)
            raise e

    def extract_data(self, testcase_extract, response):
        pattern_lst = ['(.+?)', '(.*?)', r'(\d+)', r'(\d*)']
        for key in testcase_extract:
            # 正则处理
            value = testcase_extract[key]
            if isinstance(value, dict):
                for pattern in pattern_lst:
                    if pattern in value:
                        ext_list = re.search(value, response)
                        if pattern in [r'(\d+)', r'(\d*)']:
                            ext_value = {key: int(ext_list.group(1))}
                        else:
                            ext_value = {key: ext_list.group(1)}
                        log.info(f'ext_value: {ext_value}')
                        self.ry.write_Yaml_data(ext_value)
            else:
                # json处理
                if value.startswith('$.'):
                    ext_json = jsonpath.jsonpath(json.loads(response), value)[0]
                    ext_value = {key: ext_json}
                    log.info(f'ext_value: {ext_value}')
                    self.ry.write_Yaml_data(ext_value)

    def extract_data_list(self, testcase_extract_list, response):
        pattern_lst = ['(.+?)', '(.*?)', r'(\d+)', r'(\d*)']
        for key in testcase_extract_list:
            # 正则处理
            value = testcase_extract_list[key]
            if isinstance(value, dict):
                for pattern in pattern_lst:
                    if pattern in value:
                        ext_list = re.findall(value, response)
                        if ext_list:
                            ext_value = {key: ext_list}
                        log.info(f'ext_value: {ext_value}')
                        self.ry.write_Yaml_data(ext_value)
            else:
                # json处理
                if value.startswith('$.'):
                    ext_json = jsonpath.jsonpath(json.loads(response), value)
                    ext_value = {key: ext_json}
                    log.info(f'ext_value: {ext_value}')
                    self.ry.write_Yaml_data(ext_value)


if __name__ == '__main__':
    testcase = ReadYaml().get_testcase_from_yaml('../testcase/Login/loginTestcase.yml')
    print(testcase[0])
    base = BaseRequestUtil()
    base.specification_yaml(testcase[0])

    # base = BaseRequestUtil()
    # base.replace_load(testcase)
