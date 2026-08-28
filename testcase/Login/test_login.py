import pytest
from common.readYaml import ReadYaml
from common.recordLog import log
class TestLogin(object):

    def test_login(self):
        print('登录')

    @pytest.mark.skip
    @pytest.mark.run(order=3)
    def test_login_01(self):
        print('登录03')
        assert 1>2


    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('params', [{"name","joe"},{"name","joy"}])
    def test_login_02(self,params):
        print('登录01')
        print(params)

    @pytest.mark.run(order=1)
    def test_login_03(self):
        print('登录02')

class TestLogin02(object):
    @pytest.mark.parametrize('params', ReadYaml().get_testcase_from_yaml('./testcase/Login/loginTestcae.yml'))
    def test_login_04(self,params):
        print(params)
        print(type(params))
        url = "http://127.0.0.1:8787"+params['baseInfo']['url']
        print(url)
        print(type(url))
        log.info(f'获取到的接口地址：{url}')

