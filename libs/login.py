# -*- coding: utf-8 -*-
# @Author  zhaojiaoyang
# @date  2023/7/5 21:23
# @version  1.0


from common.baseAPI import BaseAPI
from utils.handle_data import get_md5_data
from utils.handle_test import show_time

class Login(BaseAPI):
    # @show_time
    def login(self, in_data, get_token=False):
        in_data['password'] = get_md5_data(in_data['password'])
        resp_data = self.request_send(data=in_data)
        if get_token:
            return resp_data['data']['token']
        return resp_data  # 调用发送


if __name__ == '__main__':
    test_data = {
        'username': 'ct0958',
        'password': '14443'
    }
    # login = Login()
    # print(login)
    test = show_time(Login().login)(test_data, get_token=True)
    # test(test_data, get_token=True)


