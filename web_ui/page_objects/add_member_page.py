'''
@Project ：WeWork
@File ：add_member_page.py
@Author ：RZ
@Date ：2022/3/14 11:42 AM
'''
import logging
from time import sleep

import allure
from selenium.webdriver.common.by import By

from web_ui.page_objects.base import BasePage


@allure.feature('添加成员')
class AddMember(BasePage):
    _USERNAME = (By.ID, 'username')
    _ACCTID = (By.ID, 'memberAdd_acctid')
    _PHONE = (By.ID, 'memberAdd_phone')
    _SAVEBTN = (By.CSS_SELECTOR, '.js_btn_save')

    @allure.story('填写成员信息')
    def fill_info(self, name, acctid, mobile_phone):
        from web_ui.page_objects.contact_page import ContactPage

        sleep(1)
        with allure.step('输入姓名'):
            self.send_keys(*self._USERNAME, name)
            logging.info('输入姓名')
        with allure.step('输入身份证'):
            self.send_keys(*self._ACCTID, acctid)
            logging.info('输入身份证')
        with allure.step('输入手机号'):
            self.send_keys(*self._PHONE, mobile_phone)
            logging.info('输入手机号')
        with allure.step('点击保存按钮'):
            self.find_eles(*self._SAVEBTN)[0].click()
            logging.info('点击保存按钮')
        sleep(2)
        with allure.step('页面跳转到通讯录页'):
            logging.info('页面跳转到通讯录页')
            return ContactPage(self.driver)
