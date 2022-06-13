import pytest


@pytest.fixture(scope="class", autouse=True)
def class_message():
    """
        设置每一个类开始和结束分别打印message
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



