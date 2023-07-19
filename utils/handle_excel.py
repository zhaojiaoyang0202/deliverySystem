# -*- coding: utf-8 -*-
# @Author  zhaojiaoyang
# @date  2023/7/6 20:49
# @version  1.0


'''
 pip install xlrd

返回
    - 请求体数据
    - 预期响应数据
'''

import xlrd
import json
from utils.handle_yaml import get_yaml_data
def get_excel_data(sheet_name, case_name, *args, run_case = None):
    '''
    :param file_path:文件路径
    :param sheet_name:具体操作的sheet名
    :return:[(),()]
    '''
    if run_case is None:
        run_case = ['all']

    res_list = []#存放结果的

    file_path = '../data/Delivery_System_V1.5.xls'
    #excel_path = get_yaml_data('')

    work_book = xlrd.open_workbook(file_path, formatting_info=True)

    work_sheet = work_book.sheet_by_name(sheet_name)

    #---------------列名--转化--列下标------------
    # args = ['标题', '请求参数', '响应预期结果']
    col_indexs = []  # 列表
    for col_name in args:
        col_indexs.append(work_sheet.row_values(0).index(col_name))
    # print('需要获取的列名', col_indexs)


    #--------------用例筛选----------------
    # 组合型 ['all','003','005-007','009']
    run_case_list = []    # 需要运行的用例
    if 'all' in run_case:
        run_case_list = work_sheet.col_values(0)
    else:
        for one in run_case:
            if '-' in one:  # 连续的一段用例
                start, end = one.split('-')
                for i in range(int(start), int(end)+1):
                    run_case_list.append(case_name+f'{i:0>3}')
            else:
                run_case_list.append(case_name+f'{one:0>3}')

    # 3-获取指定数据
    row_idx = 0
    for one in work_sheet.col_values(0):
        if case_name in one and one in run_case_list:
            col_datas = []  # 每一行所有获取的列数据
            for num in col_indexs:
                temp = is_json(work_sheet.cell(row_idx, num).value)
                col_datas.append(temp)
            res_list.append(tuple(col_datas))
        row_idx += 1


    return res_list


def is_json(in_str):
    try:
        return json.loads(in_str)
    except:
        return in_str

if __name__ == '__main__':
    res = get_excel_data('登录模块', 'Login', *['用例编号'], run_case=['all', '001', '003-004'])
    print(res)
