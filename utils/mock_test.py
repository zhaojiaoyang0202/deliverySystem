# -*- coding: utf-8 -*-
# @Author  zhaojiaoyang
# @date  2023/7/18 9:48
# @version  1.0
import time

HOST = 'http://127.0.0.1:9999'
import requests

#-----------1,提交申请接口-------------
def commit_order(data):
    url = f'{HOST}/api/order/create/'
    payload = data
    resp = requests.post(url, json=payload)
    return resp.json()


#----------2,查询接口-----------------

def get_order_result(order_id, interval=5, end_time=30):
    url = f'{HOST}/api/order/get_result_xx/'
    payload = {'order_id': order_id}

    start_time = time.time()
    end_time = start_time + end_time
    cnt = 1
    while time.time() < end_time:
        resp = requests.get(url, params=payload)
        if resp.text:
            print('查询成功，查询结果为：'+resp.text)
            return resp.text
        else:
            print(f'第{cnt}次查询，查询失败')
            time.sleep(interval)
            cnt += 1
    # return resp.text

import threading
if __name__ == '__main__':
    start_time = time.time()
    order_data = {
        'user_id': 'sq123456',
        'goods_id': '20200815',
        'num': 1,
        'amount': 200.6
    }
    # 获取响应数据
    order_id = commit_order(order_data)['order_id']

    t1 = threading.Thread(target=get_order_result, args=(order_id,))
    t1.daemon = True
    t1.start()

    # get_order_result(order_id)

    # ------------模拟一个主线程用例执行------------
    for one in range(20):
        print(f'{one}---我正在执行主线程的自动化测试用例---')
        time.sleep(1)

    end_time = time.time()
    print('主线程花费时间为：', end_time-start_time)






