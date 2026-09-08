import pytest
import allure
from common.readYaml import ReadYaml
from common.recordLog import log
from base.apiUtils import BaseRequestUtil

# class TestLogin(object):
#
#     def test_login(self):
#         print('登录')
#
#     @pytest.mark.skip
#     @allure.story('登录01')
#     @pytest.mark.run(order=3)
#     def test_login_01(self):
#         print('登录03')
#         assert 1>2
#         allure.attach('登录01')
#
#
#     @pytest.mark.run(order=1)
#     @allure.story('登录02')
#     @pytest.mark.parametrize('params', [{"name","joe"},{"name","joy"}])
#     def test_login_02(self,params):
#         print('登录01')
#         print(params)
#         allure.attach('登录02')
#
#     @pytest.mark.run(order=1)
#     @allure.story('登录03')
#     def test_login_03(self):
#         print('登录02')
#         allure.attach('登录03')

@allure.feature('登录接口')
class TestLogin02(object):
   case_info = ReadYaml().get_testcase_from_yaml('./testcase/Login/loginTestcase.yml')

   @pytest.mark.parametrize('params', case_info)
   @allure.story('正确的用户名和密码')
   def test_login_04(self,params):
        print(params)
        print('params',type(params))
        BaseRequestUtil().specification_yaml(params)

