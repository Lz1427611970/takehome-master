import os
import yaml


def get_test_yaml(file_path):
    """
        获取yaml文件
    """
    # 获取并添加test_yaml的路径
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_data')
    # 获取并添加yaml的路径
    yaml_path = os.path.join(path, file_path)
    # 读取yaml文件
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    yaml_case = get_test_yaml(file_path='test_normal_yaml.yaml')
    print(yaml_case)
