# -*- coding: utf-8 -*-
# @Author  zhaojiaoyang
# @date  2023/7/5 20:56
# @version  1.0


import yaml
def get_yaml_data(file_path:str):
    with open(file_path, encoding='utf-8') as f:
        return yaml.safe_load(f.read())



if __name__ == '__main__':
    res = get_yaml_data('../configs/apiPathConfig.yml')
    print(res)


