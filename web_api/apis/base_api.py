'''
@Project ：WeWork
@File ：base_api.py
@Author ：RZ
@Date ：2022/3/21 9:30 PM
'''
import logging

import requests


class BaseApi:
    # 设置 loging
    # 指定 log 日志的存放位置（需要先创建目录，否则会报错）
    # 指定日志的编码格式
    fileHandler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    # 设置日志的等级
    logging.getLogger().setLevel(0)
    # 设置日志的内容格式
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    fileHandler.setFormatter(formatter)
    # 设置生效
    logging.getLogger().addHandler(fileHandler)

    def log_info(self, msg):
        return logging.info(msg)

    def send_api(self, req):
        self.log_info("----------------requests data----------------")
        self.log_info(req)
        r = requests.request(**req)
        self.log_info("----------------response data----------------")
        self.log_info(r.json())
        return r
