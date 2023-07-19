# @Author  zhaojiaoyang
# @date  2023/6/8 20:56
# @version  1.0

import os
"""
需求：在很多自动化执行的环境中，由于使用相对路径，它对切入的当前路径要求很高，不然在代码里写的哪些所谓的相对路径都会报错
解决方案：
    代码自动获取项目路径，其他路径根据项目路径去查找！
"""
#当前执行的文件
# print(__file__)
#获取上一层目录
# print(os.path.dirname(__file__))
#获取上上一层目录
# print(os.path.dirname(os.path.dirname(__file__)))
#工程路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print('项目工程路径>>>', project_path)
#配置路径
config_path = os.path.join(project_path, 'configs')
# print('配置路径>>>', config_path)
#测试数据路径
data_path = os.path.join(project_path, 'data')
# print('测试数据路径>>>', data_path)
#测试报告路径
report_path = os.path.join(project_path, r'outFiles\report\tmp')
# print('测试报告路径>>>', report_path)
#日志路径
log_path = os.path.join(project_path, r'outFiles\log')
# print('日志路径>>>', log_path)


