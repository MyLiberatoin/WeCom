'''
@Project ：WeWork 
@File ：contact_page.py
@Author ：RZ
@Date ：2022/4/3 12:12 PM 
'''
import logging

from appium.webdriver.common.appiumby import AppiumBy

from app_ui.base.base import BasePage
from app_ui.page.addlist_page import AddList


class ContactPage(BasePage):
    _ADD_MEMBER = (AppiumBy.XPATH, '//*[@text="添加成员"]')

    def click_addbtn(self):
        logging.info("滑动页面，点击添加成员")
        self.scroll_click(*self._ADD_MEMBER, 5)
        logging.info("跳转到添加成员页面")
        return AddList(self.driver)
