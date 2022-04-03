'''
@Project ：WeWork 
@File ：app.py
@Author ：RZ
@Date ：2022/4/3 12:15 PM 
'''
import logging

import yaml
from appium import webdriver


class App:
    def start(self):
        logging.info("读取设备配置信息")
        with open("../data/config.yaml", "r") as f:
            desire_cap = yaml.safe_load(f)
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(3)
        return self

    def stop(self):
        logging.info("退出app")
        self.driver.quit()

    def lauch_main(self):
        from app_ui.page.main_page import MainPage
        logging.info("进入首页")
        return MainPage(self.driver)
