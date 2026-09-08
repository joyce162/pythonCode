import jsonpath
import allure

from common.readYaml import ReadYaml
from common.recordLog import log
from common.connection import ConnectMysql


class Assertions:

    def assert_result(self, expected, response, status_code):
        all_flag = 0
        try:
            if status_code != 200:
                all_flag = 1
                log.error('断言失败，status_code：%s' % (status_code))
                allure.attach(status_code, f'测试失败，status_code：{status_code}', attachment_type=allure.attachment_type.TEXT)
            else:
                for i in expected:
                    if 'contains' in i.keys():
                        all_flag = self.contains_assert(i, response)
                    elif 'eq' in i.keys():
                            pass
                    elif 'sql' in i.keys():
                        all_flag = self.sql_assertion(i)
        except Exception as e:
            all_flag = 1
            log.error(e)
        assert all_flag==0

    def contains_assert(self, validationValue, response):
        """
        该方法为
        :param validationValue: 预期结果，为字典
        :param response:实际结果
        :return: flag=0,断言成功。flag为其他值则断言失败
        """
        flag = 0
        for key, value in validationValue.items():
            jsonpathValue = value.pop('jsonPath')
            resp_list = jsonpath.jsonpath(response, jsonpathValue)
            for k,v in value.items():
                if resp_list:
                    if v in resp_list:
                        log.info('断言通过，预期结果: %s，实际结果：%s' % (v, str(resp_list)))
                        allure.attach(str(resp_list), f'测试通过，预期结果：{v}，实际结果：{str(resp_list)}',
                                      attachment_type=allure.attachment_type.TEXT)
                    else:
                        flag += 1
                        log.error('断言失败，预期结果: %s，实际结果：%s' % (v, str(resp_list)))
                        allure.attach(str(resp_list), f'测试失败，预期结果：{v}，实际结果：{str(resp_list)}',
                                      attachment_type=allure.attachment_type.TEXT)
                else:
                    flag += 1
                    log.error('断言失败，预期结果: %s，实际结果：为空' % (v))
                    allure.attach(f'测试通过，预期结果：{v}，实际结果：为空',
                                  attachment_type=allure.attachment_type.TEXT)
        return flag

    def sql_assertion(self,sqlValidation):
        """
        数据库断言
        :param sqlValidation: 格式是字典{'sql':''}
        :return: 返回flag，flag=0则测试通过，其他则测试不通过
        """
        flag = 0
        sql = sqlValidation['sql']
        conn = ConnectMysql()
        res = conn.query(sql)
        if res is None:
            flag+=1
            log.info('数据库断言失败，查询结果为空')
            allure.attach('数据库断言失败，查询结果为空',attachment_type=allure.attachment_type.TEXT)
        return flag


if __name__ == '__main__':
    assertions = Assertions()

    testcase = ReadYaml().get_testcase_from_yaml('../testcase/Login/loginTestcase.yml')[0]['testcase']
    validation_list = testcase[0]['validation']
    response = {
        'msg': '登录成功',
        'errorCode': 200
    }

    assertions.assert_result(validation_list, response,200)
