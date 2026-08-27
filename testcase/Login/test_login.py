import pytest
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
