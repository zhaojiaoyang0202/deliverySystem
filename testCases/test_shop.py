# -*- coding: utf-8 -*-
# @Author  zhaojiaoyang
# @date  2023/7/12 14:25
# @version  1.0


import pytest
import allure
from utils.handle_excel import get_excel_data
# 创建测试类--业务模块--逻辑处理

'''
店铺模块的测试
1.首先完成有效的登录操作----拿到token
2.完成店铺实例的创建

'''

@allure.epic('外卖系统')
@allure.feature('店铺模块')
# 创建测试类
class TestShop:
    # 创建测试方法---对应模块里具体的接口
    @pytest.mark.parametrize('title,req_body,exp_resp', get_excel_data('我的商铺', 'listshopping', '标题', '请求参数', '响应预期结果'))
    @allure.story('店铺查询')
    @allure.title('{title}')
    def test_shop_query(self, shop_init, title, req_body, exp_resp):
        res = shop_init.query(req_body)
        assert res['code'] == exp_resp['code']


    # -----------方案1----------------
    # @pytest.mark.parametrize('title,req_body,exp_resp', get_excel_data('我的商铺', 'updateshopping', '标题', '请求参数', '响应预期结果'))
    # @allure.story('店铺查询')
    # @allure.title('{title}')
    # def test_shop_update(self, shop_init, title, req_body, exp_resp):
    #     # 涉及到多个接口关联的接口场景，在allure报告里可以写出操作步骤！
    #     with allure.step('1.用户登录'):
    #         # shop_object = shop_init
    #         pass
    #     with allure.step('2.选中编辑店铺'):
    #         shop_id = shop_init.query({'page': 1, 'limit': 20})['data']['records'][0]['id']
    #     with allure.step('3.替换店铺图片'):
    #         image_info = shop_init.file_upload('../data/123.png')['data']['realFileName']
    #     with allure.step('4.提交店铺信息'):
    #         res = shop_init.update(req_body, shop_id, image_info)
    #     with allure.step('5.判断是否操作成功'):
    #         assert res['code'] == exp_resp['code']


    #-------------方案2--------------
    @pytest.mark.parametrize('title,req_body,exp_resp',
                             get_excel_data('我的商铺', 'updateshopping', '标题', '请求参数', '响应预期结果'))
    @allure.story('店铺查询')
    @allure.title('{title}')
    def test_shop_update(self, shop_update_init,  title, req_body, exp_resp):
        # 涉及到多个接口关联的接口场景，在allure报告里可以写出操作步骤！
        with allure.step('4.提交店铺信息'):
            res = shop_update_init['shop_init'].update(req_body, shop_update_init['shop_id'], shop_update_init['image_info'])
        with allure.step('5.判断是否操作成功'):
            assert res['code'] == exp_resp['code']




if __name__ == '__main__':
    # pytest.main([__file__,'-sv'])

    import os

    pytest.main([__file__, '-s', '--alluredir', '../outFiles/report/tmp', '--clean-alluredir'])
    os.system('allure serve ../outFiles/report/tmp')

