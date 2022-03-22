'''
@Project ：WeWork
@File ：base.py
@Author ：RZ
@Date ：2022/3/14 11:42 AM
'''
import logging
from time import sleep

import allure
import yaml
from selenium import webdriver


class BasePage:
    @allure.story('准备环境，注入cookie')
    def __init__(self, driver=None):
        # 实例化webdriver
        if driver is None:
            self.driver = webdriver.Chrome()
            logging.info('实例化webdriver')
            self.driver.implicitly_wait(3)
            logging.info('隐式等待3s')
            self.driver.maximize_window()
            logging.info('窗口最大化')
            with allure.step('进入首页'):
                self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
                logging.info('不能直接进入首页，系统会重定向到登录页')

            # 获取cookie并写入yaml文件
            # with open('../data/cookie.yaml', 'w+') as f:
            #     sleep(20)
            #     cookies = self.driver.get_cookies()
            #     yaml.safe_dump(cookies, f)

            # 注入cookie
            with allure.step('注入cookie'):
                with open('../data/cookie.yaml', 'r') as f:
                    cookies = yaml.safe_load(f)
                    for c in cookies:
                        self.driver.add_cookie(c)
                    logging.info('注入cookie')
                    self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
                    logging.info('页面跳转到首页')
        else:
            self.driver = driver

    def send_keys(self, by, ele, value):
        self.driver.find_element(by, ele).send_keys(value)

    def do_click(self, by, ele):
        self.driver.find_element(by, ele).click()

    def find_eles(self, by, ele):
        return self.driver.find_elements(by, ele)
