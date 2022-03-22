'''
@Project ：WeWork
@File ：main_page.py
@Author ：RZ
@Date ：2022/3/14 11:42 AM
'''
import logging

import allure
from selenium.webdriver.common.by import By

from web_ui.page_objects.base import BasePage


@allure.feature('进入首页')
class MainPage(BasePage):
    _ADDBTN = (By.CSS_SELECTOR,
               '#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(1)')
    _CONTACTLINK = (By.ID, 'menu_contacts')

    @allure.story('点击添加成员图标')
    def click_add_btn(self):
        # 一定要在方法里面导入
        from web_ui.page_objects.add_member_page import AddMember
        # *解包
        with allure.step('点击添加成员图标'):
            logging.info('点击添加成员图标')
            self.do_click(*self._ADDBTN)
            logging.info('页面跳转到添加成员页')
        return AddMember(self.driver)

    @allure.story('点击通讯录导航')
    def go_to_contact(self):
        with allure.step('点击通讯录选项'):
            self.do_click(*self._CONTACTLINK)
            logging.info('点击通讯录选项')
        with allure.step('跳转到通讯录页'):
            from web_ui.page_objects.contact_page import ContactPage
            logging.info('跳转到通讯录页')
            return ContactPage(self.driver)
