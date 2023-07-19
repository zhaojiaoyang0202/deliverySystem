# -*- coding: utf-8 -*-
# @Author  zhaojiaoyang
# @date  2023/7/3 21:27
# @version  1.0


# md5_加密
import base64
import hashlib   # 不需要安装---内置库

def get_md5_data(pwd:str,salt=''):
    '''
    :param pwd:加密得字符串
    :param salt:盐值
    :return:返回加密后得结果
    '''
    # 1-创建md5实例
    md5 = hashlib.md5()
    # 2-调用加密方法
    pwd = pwd+salt  # 拼接盐值
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()   # 加密后得结果  ---16进制


# 加密环境
# pip install pycryptodome -i https://douban.com/simple

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher



from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher


class RsaEndecrypt:
    def __init__(self, filepath='./'):
        self.filepath = filepath


    def encrypt(self,data):
        with open(self.filepath+'public_login.pem', 'rb') as f:
            public_content = f.read()
            publickey = RSA.importKey(public_content)
            cipher = PKCS1_cipher.new(publickey)
            cipher_text = cipher.encrypt(data.encode('utf-8'))
            return base64.b64encode(cipher_text).decode()


    def encrypt2(self, crypt_data):
        with open(self.filepath+'public.pem') as f:
            key = f.read()
            public_key = RSA.importKey(key)
            cipher = PKCS1_cipher.new(public_key)
            rsa_text = base64.b64encode(cipher.encrypt(bytes(crypt_data.encode('utf-8'))))
            return rsa_text


    def decrypt(self, text):
        with open(self.filepath + 'private.pem', 'rb') as op:
            private_key = op.read()
            """校验RSA加密 使用私钥进行解密"""
            cipher = PKCS1_cipher.new(RSA.importKey(private_key))
            retval = cipher.decrypt(base64.b64decode(text), 'ERROR').decode('utf-8')
            return retval



if __name__ == '__main__':
    test_flag = 5
    if test_flag == 5:
        deres = RsaEndecrypt().decrypt('123456')
        print(deres)

    if test_flag == 4:
        enres = RsaEndecrypt().encrypt('123456')
        deres = RsaEndecrypt().decrypt(enres)
        print(enres)
        print(deres)

    if test_flag == 3:
        res = RsaEndecrypt().encrypt2('123456')
        res2 = RsaEndecrypt().decrypt(res)
        print(res)
        print(res2)

    if test_flag == 2:
        res = RsaEndecrypt().encrypt('123456')
        print(res)

    if test_flag == 1:
        res = get_md5_data('xintian')
        print(res)




















