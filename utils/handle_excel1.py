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
def get_excel_data(file_path, sheet_name):
    '''

    :param file_path:文件路径
    :param sheet_name:具体操作的sheet名
    :return:[(),()]
    '''
    res_list = []#存放结果的
    # 1-打开excel文件
    # formatting_info 指定原样式
    work_book = xlrd.open_workbook(file_path, formatting_info=True)

    # 2-指定对应的表
    # print(work_book.sheet_names())   # 查看所有的表名
    # print(work_book.sheet_by_name(sheet_name))      # 根据sheet_name查看对应的的sheet

    work_sheet = work_book.sheet_by_name(sheet_name)
    # print(work_sheet.row_values(0))   # 打印一行数据
    # print(work_sheet.col_values(0))

    # 3-获取指定数据
    row_idx = 0
    for one in work_sheet.col_values(0):
        req_body = work_sheet.cell(row_idx, 9).value  # cell(行编号，列编号)
        resp_data = work_sheet.cell(row_idx, 11).value
        row_idx += 1
        res_list.append((req_body, resp_data))

    return res_list

if __name__ == '__main__':
    res = get_excel_data('../data/Delivery_System_V1.5.xls', '登录模块')
    print(res)
