'''
@Project ：WeWork 
@File ：main_page.py
@Author ：RZ
@Date ：2022/4/3 12:12 PM 
'''
import logging

from appium.webdriver.common.appiumby import AppiumBy

from app_ui.base.base import BasePage
from app_ui.page.contact_page import ContactPage


class MainPage(BasePage):
    _CONTACT = (AppiumBy.XPATH, '//*[@text="通讯录"]')

    def click_contact(self):
        logging.info("点击通讯录菜单")
        self.find_click(*self._CONTACT)
        logging.info("跳转到通讯录页面")
        return ContactPage(self.driver)
