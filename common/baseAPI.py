# -*- coding: utf-8 -*-
# @Author  zhaojiaoyang
# @date  2023/7/5 20:03
# @version  1.0



# 这个基类后续可能因为业务模块的增加可以维护
import traceback

print()
'''
封装思路：
    1-为所有的业务模块提供的基本接口操作：增删改查+发送接口
    2-日志  截图都可以在基类里封装
    3-断言方法

'''
import requests
import inspect
from utils.handle_yaml import get_yaml_data
from configs.config import HOST
from utils.handle_loguru import log
class BaseAPI:
    def __init__(self, token=None):
        if token: # 需要token业务
            self.header = {'Authorization': token}
        else:
            self.header = None
        # 获取对应模块的接口信息
        self.data = get_yaml_data('../configs/apiPathConfig.yml')[self.__class__.__name__]


    # 1- 发送的公共方法，每一个接口都会调用它
    def request_send(self, data=None, params=None, files=None, id=''):
        try:
            api_data = self.data[inspect.stack()[1][3]]
            resp = requests.request(
                method=api_data['method'],
                url=f'{HOST}{api_data["path"]}{id}',
                data=data,
                params=params,
                files=files,
                headers=self.header
            )

            # ---------log里面输出请求信息-info级别--------
            # 日志信息：业务模块+具体接口+接口信息
            log_msg = f'''模块名:{self.__class__.__name__},接口名:{inspect.stack()[1][3]}
    请求的url:{resp.request.url}
    请求方法:{resp.request.method}
    请求体:{resp.request.body}
    响应体:{resp.json()}'''
            log.info(log_msg)

            # log.info(f'模块名:{self.__class__.__name__},接口名:{inspect.stack()[1][3]}')
            # log.info(f'请求的url:{resp.request.url}')
            # log.info(f'请求方法:{resp.request.method}')

            return resp.json()

        except Exception as error:
            log.error(traceback.format_exc())
            raise error


    #-------------增删改查----------------
    def query(self, data):
        return self.request_send(params=data)

    def add(self, data):
        return self.request_send(params=data)

    def update(self, data):
        return self.request_send(params=data)

    def delete(self, id):
        return self.request_send(id=id)

    # 'http://192.0.0.1:8080/s/6'


    #--------------文件上传---------------
    '''
    文件上传格式：  文件路径，文件名，文件类型
    路径：xx/123.png
    {'file':('123.png',open('xx/123.png','rb'),'png')}
    '''
    def file_upload(self, file_path: str):
        # 1-获取文件名
        file_name = file_path.split('/')[-1]
        # 2-文件类型
        file_type = file_path.split('.')[-1]
        file = {'file': (file_name, open(file_path, 'rb'), file_type)}
        # 3-发送请求
        return self.request_send(files=file)






# ------------------演示案例-----------------
# import inspect
# def send():
#     print(f'----{inspect.stack()[1][3]}调用send方法----')
#
#
# def login():
#     print('---函数login开始执行了---')
#     send()
#
# login()



