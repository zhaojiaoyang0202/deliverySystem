# -*- coding: utf-8 -*-
# @Author  zhaojiaoyang
# @date  2023/7/10 9:49
# @version  1.0
import allure
import pytest
from libs.login import Login
from utils.handle_excel import get_excel_data
from common.apiAssert import ApiAssert


@allure.epic('订餐系统')
@allure.feature('登录模块')
# 1-登录类
class TestLogin:
    # 2-登录的方法
    @pytest.mark.parametrize('title,body,exp_data', get_excel_data('登录模块', 'Login', '标题', '请求参数', '响应预期结果'))
    @allure.story('登录接口')
    @allure.title('{title}')
    def test_login(self, title, body, exp_data):
        # print(body, exp_data)
        # 3-调用登录的接口
        res = Login().login(body)
        # 4-断言结果是否符合预期
        # assert res['msg'] == exp_data['msg']
        ApiAssert.api_assert(res, '==', exp_data, assert_info='msg', msg='登录接口断言')
        # ApiAssert.api_assert(res, '==', exp_data, assert_info='code', msg='登录接口断言')

if __name__ == '__main__':
    pytest.main([__file__, '-sv'])
    # import os
    # pytest.main([__file__, '-s', '--alluredir', '../outFiles/report/tmp', '--clean-alluredir'])
    # os.system('allure serve ../outFiles/report/tmp')

