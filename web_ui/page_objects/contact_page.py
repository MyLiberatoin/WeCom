'''
@Project ：WeWork
@File ：contact_page.py
@Author ：RZ
@Date ：2022/3/14 11:42 AM
'''
import logging
from time import sleep

import allure
from selenium.webdriver.common.by import By

from web_ui.page_objects.base import BasePage


@allure.feature('查看成员信息')
class ContactPage(BasePage):
    _NAMES = (By.CSS_SELECTOR, '#member_list > tr > td:nth-child(2) > span:nth-child(1)')
    _ADDMEMBER = (By.CSS_SELECTOR, 'a.qui_btn.ww_btn.js_add_member')

    @allure.story('获取成员姓名')
    def check_info(self):
        # 获取通讯录所有成员的姓名
        with allure.step('获取通讯录所有成员的姓名'):
            ele = self.find_eles(*self._NAMES)
            names = []
            for i in ele:
                names.append(i.text)
            logging.info('获取通讯录所有成员的姓名')
            return names

    @allure.story('点击添加成员按钮')
    def click_add_btn(self):
        with allure.step('点击添加成员按钮'):
            sleep(1)
            logging.info('点击添加成员按钮')
            self.find_eles(*self._ADDMEMBER)[1].click()
            sleep(1)
            logging.info('跳转到添加成员页面')
            from web_ui.page_objects.add_member_page import AddMember
            return AddMember(self.driver)
