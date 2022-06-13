import pytest

if __name__ == '__main__':
    """
        指定用例等级，并运行主函数
    """
    lv = "P0"
    pytest.main(['-vs', '-m', f'{lv}'])