import pytest
# 导入获取yaml文件
from test.test_cal.common.get_test_yaml import get_test_yaml
# 导入Calculate类
from test.calculate import Calculate

# 导入正常case的yaml文件
yaml_normal_case = get_test_yaml(file_path='test_normal_yaml.yaml')


class TestNormalCase(object):
    """
        测试Calculate正常case
    """
    @pytest.mark.P0
    @pytest.mark.parametrize('a,b,c', [(yaml_normal_case['case_01'][0], yaml_normal_case['case_01'][1], yaml_normal_case['case_01'][2])])
    def test_01(self, a, b, c):
        assert Calculate().cal(a=a, b=b, c=c) == yaml_normal_case['case_01'][3]

    @pytest.mark.P0
    @pytest.mark.parametrize('a,b,c', [(yaml_normal_case['case_02'][0], yaml_normal_case['case_02'][1], yaml_normal_case['case_02'][2])])
    def test_02(self, a, b, c):
        assert Calculate().cal(a=a, b=b, c=c) == yaml_normal_case['case_02'][3]

    @pytest.mark.P0
    @pytest.mark.parametrize('a,b,c', [(yaml_normal_case['case_03'][0], yaml_normal_case['case_03'][1], yaml_normal_case['case_03'][2])])
    def test_03(self, a, b, c):
        assert Calculate().cal(a=a, b=b, c=c) == yaml_normal_case['case_03'][3]


if __name__ == '__main__':
    pytest.main('-vs')
