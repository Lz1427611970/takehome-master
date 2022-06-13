import pytest
# 导入获取yaml文件
from test.test_cal.common.get_test_yaml import get_test_yaml
# 导入Calculate类
from test.calculate import Calculate

# 导入异常case的yaml文件
yaml_abnormal_case = get_test_yaml(file_path='test_abnormal_yaml.yaml')


# 异常入参这里应该要测下分别异常的case组合的情况，
# 第一次用yaml没想好怎么组合，之前只用过多装饰器生成笛卡尔积组合的脚本，需要优化下。
class TestAbnormalCase(object):
    """
        测试Calculate异常case
    """
    @pytest.mark.P1
    @pytest.mark.parametrize('a,b,c', [(yaml_abnormal_case['case_01'][0], yaml_abnormal_case['case_01'][1], yaml_abnormal_case['case_01'][2])])
    def test_01(self, a, b, c):
        assert Calculate().cal(a=a, b=b, c=c) == yaml_abnormal_case['case_01'][3]

    @pytest.mark.P1
    @pytest.mark.parametrize('a,b,c', [(yaml_abnormal_case['case_02'][0], yaml_abnormal_case['case_02'][1], yaml_abnormal_case['case_02'][2])])
    def test_02(self, a, b, c):
        assert Calculate().cal(a=a, b=b, c=c) == yaml_abnormal_case['case_02'][3]

    @pytest.mark.P1
    @pytest.mark.parametrize('a,b,c', [(yaml_abnormal_case['case_03'][0], yaml_abnormal_case['case_03'][1], yaml_abnormal_case['case_03'][2])])
    def test_03(self, a, b, c):
        assert Calculate().cal(a=a, b=b, c=c) == yaml_abnormal_case['case_03'][3]

    @pytest.mark.P1
    @pytest.mark.parametrize('a,b,c', [(yaml_abnormal_case['case_04'][0], yaml_abnormal_case['case_04'][1], yaml_abnormal_case['case_04'][2])])
    def test_04(self, a, b, c):
        assert Calculate().cal(a=a, b=b, c=c) == yaml_abnormal_case['case_03'][3]


if __name__ == '__main__':
    pytest.main('-vs')
