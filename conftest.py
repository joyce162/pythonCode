import pytest
@pytest.fixture(scope="session", autouse=True)
def fixture_test():
    print('--------------前置开始--------------')
    yield
    print('--------------后置结束--------------')