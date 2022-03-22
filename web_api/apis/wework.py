'''
@Project ：WeWork
@File ：wework.py
@Author ：RZ
@Date ：2022/3/21 9:23 PM
'''
from web_api.apis.base_api import BaseApi


class WeWork(BaseApi):
    def __init__(self, corpid, corpsecret):
        self.token = self.get_token(corpid, corpsecret)['access_token']
        self.log_info("获取access_token")

    def get_token(self, corpid, corpsecret):
        req = {
            "method": 'GET',
            "url": f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
        }
        r = self.send_api(req)
        return r.json()
