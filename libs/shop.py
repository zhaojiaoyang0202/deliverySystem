# -*- coding: utf-8 -*-
# @Author  zhaojiaoyang
# @date  2023/7/10 19:57
# @version  1.0


from common.baseAPI import BaseAPI
from libs.login import Login

class Shop(BaseAPI):
    # 重新编辑接口
    '''
    1-需要动态获取店铺的有效id
    2-需要动态获取图片信息
    '''
    def update(self, data, shop_id, image_info):
        # 1-更新id
        if data['id'] != '0000':
            data['id'] = shop_id

        # 2-更新图片信息
        data['image_path'] = image_info
        data['image'] = f'/file/getImgStream?fileName={image_info}'
        # 3-调用父类的update发送
        return super().update(data)













if __name__ == '__main__':
    pass
    # test_data = {'page': 1, 'limit': 20}
    # resp = Shop().shop_query(test_data)
    # print(resp)

    #1- 登录操作
    login_data = {'username': 'th0198', 'password': 'xintian'}
    token = Login().login(login_data, get_token=True)
    #2- 创建店铺实例
    shop = Shop(token)
    #3- 列出店铺
    test_data = {'page': 1, 'limit': 20}
    shop_res = shop.query(test_data)
    print('列出商铺信息---->', shop_res)
    #4- 获取店铺id
    shop_id = shop_res['data']['records'][0]['id']
    print('店铺id---->', shop_id)
    #4- 文件上传接口
    image_info = shop.file_upload('../data/123.png')
    print('列出图片信息---->', image_info)
    image_infos = image_info['data']['realFileName']
    print('列出图片信息---->', image_infos)
    #5- 店铺更新
    update_data = {
            "name": "星巴克新建店",
            "address": "上海市静安区秣陵路303号",
            "id": "id",
            "Phone": "13176876632",
            "rating": "5.0",
            "recent_order_num": 110,
            "category": "快餐便当/简餐",
            "description": "满30减5，满60减8",
            "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
            "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
        }
    resp = shop.update(update_data, shop_id, image_infos)
    print(resp)





