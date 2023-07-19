# -*- coding: utf-8 -*-
# @Author  zhaojiaoyang
# @date  2023/7/3 21:27
# @version  1.0

import time

def show_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)   # login()
        end_time = time.time()
        print(f'执行自动化测试用例使用了{end_time-start_time}')
        return res
    return inner


# @show_time
# def test():
#     print('开始执行测试用例')
#     time.sleep(1)
#     print('结束执行测试用例')


# test = show_time(test)   # 狸猫换太子
# test()
