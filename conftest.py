import pytest
from common.readYaml import ReadYaml
from common.corpwechatSendMsg import corpwechatSendMsg

ry = ReadYaml()

@pytest.fixture(scope="session", autouse=True)
def clear_extract_data():
    ry.clear_extract_yml()


@pytest.fixture(scope="session", autouse=True)
def fixture_test():
    print('--------------前置开始--------------')
    yield
    print('--------------后置结束--------------')

def pytest_terminal_summary(terminalreporter):
    total=terminalreporter._numcollected
    passed = len(terminalreporter.stats.get('passed',[]))
    failed = len(terminalreporter.stats.get('failed',[]))
    skipped = len(terminalreporter.stats.get('skipped', []))
    error = len(terminalreporter.stats.get('error', []))

    content = f"""
            各位好
            测试用例总数：{total}
            成功：{passed}
            失败：{failed}
            跳过：{skipped}
            链接：www.123.com
    """
    corpwechatSendMsg(content)