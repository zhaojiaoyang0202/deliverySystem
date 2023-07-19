# -*- coding: utf-8 -*-
# @Author  zhaojiaoyang
# @date  2023/7/13 14:26
# @version  1.0

# 1.增加断言类型，2.增加log操作
'''
断言类型：
    - =
    - in
    - not in
    - !=
    - > <
    -
'''


import traceback
from utils.handle_loguru import log
class ApiAssert:

    @classmethod
    def api_assert(cls, result, condition, exp_result, assert_info, msg='断言操作'):
        # 断言结果描述
        pass_msg = '验证通过,预期结果:{0},实际结果:{1}'
        try:
            # 断言类型
            assert_type = {
                '==': result[assert_info] == exp_result[assert_info],
                '!=': result[assert_info] != exp_result[assert_info],
                '>': result[assert_info] > exp_result[assert_info],
                '<': result[assert_info] > exp_result[assert_info],
                'in': result[assert_info] in exp_result[assert_info],
                'not in': result[assert_info] not in exp_result[assert_info],
            }

            # 使用断言类型
            if condition in assert_type:  #断言类是存在的
                assert assert_type[condition] # 操作断言
            else: # 断言类型不存在，报错，虽然代码不会报错，需要我们人为标记异常
                raise AssertionError('请输入正确的断言情况')
            log.info(f'{msg},断言类型:{condition},断言结果:{pass_msg.format(exp_result[assert_info],result[assert_info])}')
        except Exception as error:
            log.error(traceback.format_exc())
            # 在这里已经处理了异常，如果不抛出pytest不知道
            raise error
















