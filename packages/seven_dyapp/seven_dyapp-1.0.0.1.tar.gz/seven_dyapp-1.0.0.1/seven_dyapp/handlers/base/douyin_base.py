# -*- coding: utf-8 -*-
"""
@Author: HuangJianYi
@Date: 2021-01-14 10:44:07
:LastEditTime: 2021-05-13 14:45:49
:LastEditors: HuangJingCan
@Description: 
"""
import requests
import json
from Crypto.Cipher import AES
import base64
from seven_framework.base_model import *
from seven_framework.redis import *


class DouYinHelper:

    logger_error = Logger.get_logger_by_name("log_error")

    @classmethod
    def get_code_data(self, code="", anonymous_code=""):
        """
        :description:获取open_id、session_key等信息
        :param code: 登录票据,非匿名需要 code
        :param anonymous_code: 非匿名下的 anonymous_code 用于数据同步，匿名需要 anonymous_code
        :return: 
        :last_editors: HuangJingCan
        """
        redis_key = "dy_login_code:" + str(code)
        open_id = self.redis_init().get(redis_key)
        if open_id:
            return open_id.decode()

        app_id = config.get_value("app_id")
        app_secret = config.get_value("app_secret")
        param = {
            'code': code,  # 用户点击按钮跳转到抖音授权页, 抖音处理完后重定向到redirect_uri, 并给我们加上code=xxx的参数, 这个code就是我们需要的
            'appid': app_id,
            'secret': app_secret,
            'anonymous_code': anonymous_code,
        }

        # 通过code获取access_token
        openIdUrl = 'https://developer.toutiao.com/api/apps/jscode2session'
        resp = None
        try:
            resp = requests.get(openIdUrl, params=param)
            res_result = json.loads(resp.text)
            open_id = res_result['openid']
            session_key = res_result['session_key']
            union_id = res_result['unionid']
            anonymous_open_id = res_result['anonymous_openid']
            self.redis_init().set(redis_key, open_id, ex=10 * 1)
            self.redis_init().set(f"sessionkey:{str(open_id)}", session_key, ex=60 * 60)

            code_data = {}
            code_data['open_id'] = open_id
            code_data['session_key'] = session_key
            code_data['union_id'] = union_id
            code_data['anonymous_open_id'] = anonymous_open_id
            return code_data
        except Exception as ex:
            self.logger_error.error(str(ex) + "【get_jscode2session】" + str(resp.text))
            return {}

    @classmethod
    def decrypted_data(self, open_id, code, encrypted_Data, iv):
        """
        :description:解析加密数据，客户端判断是否登录状态，如果登录只传open_id不传code，如果是登录过期,要传code重新获取session_key
        :param open_id：open_id
        :param code：登录票据
        :param encrypted_Data：加密数据,抖音返回加密参数
        :param iv：抖音返回参数
        :return: 解密后的数据，用户信息或者手机号信息
        :last_editors: HuangJingCan
        """
        app_id = config.get_value("app_id")
        data = {}
        if code:
            code_data = self.get_code_data(code)
            if code_data and code_data['open_id']:
                open_id = code_data['open_id']
        try:
            session_key = self.redis_init().get(f"sessionkey:{str(open_id)}")
            if session_key:
                session_key = session_key.decode()
            data_crypt = BizDataCrypt(app_id, session_key)
            data = data_crypt.decrypt(encrypted_Data, iv)  #data中是解密的信息
        except Exception as ex:
            self.logger_error.error(str(ex) + "【decrypted_data】")

        return data

    @classmethod
    def decrypt_data(self, app_id, session_key, encrypted_Data, iv):
        """
        :description:解析加密数据
        :param app_id: 抖音小程序标识
        :param session_key: session_key调用登录接口获得
        :param encrypted_Data：加密数据,抖音返回加密参数
        :param iv：抖音返回参数
        :return: 解密后的数据，用户信息或者手机号信息
        :last_editors: HuangJingCan
        """
        data = {}
        try:
            data_crypt = BizDataCrypt(app_id, session_key)
            #data中是解密的信息
            data = data_crypt.decrypt(encrypted_Data, iv)
        except Exception as ex:
            self.logger_error.error(str(ex) + "【decrypt_data】")

        return data

    @classmethod
    def redis_init(self, db=None, decode_responses=False):
        """
        :description: redis初始化
        :return: redis_cli
        :last_editors: HuangJingCan
        """
        host = config.get_value("redis")["host"]
        port = config.get_value("redis")["port"]
        if not db:
            db = config.get_value("redis")["db"]
        password = config.get_value("redis")["password"]
        redis_cli = RedisHelper.redis_init(host, port, db, password, decode_responses)

        return redis_cli


class BizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        """
        :description: 解密
        :param encryptedData: encryptedData
        :param iv: iv
        :return str
        :last_editors: HuangJingCan
        """
        # base64 decode
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)
        decrypted = {}
        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
        result_data = str(self._unpad(cipher.decrypt(encryptedData)), "utf-8")
        if result_data:
            decrypted = json.loads(result_data)
        if decrypted:
            if decrypted['watermark']['appid'] != self.appId:
                raise Exception('Invalid Buffer')

        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]