import pytest


@pytest.fixture(scope="session", autouse=True)
def session_message():
    """
        设置每一个会话开始和结束分别打印message
    """
    print("计算开始")
    yield
    print("计算结束")


@pytest.fixture(scope='function', autouse=True)
def function_message():
    """
        设置每一个方法开始和结束分别打印message
    """
    print("测试开始")
    yield
    print("\n测试结束")



