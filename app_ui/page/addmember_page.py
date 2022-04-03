'''
@Project ：WeWork 
@File ：addmember_page.py
@Author ：RZ
@Date ：2022/4/3 12:15 PM 
'''
import logging

from appium.webdriver.common.appiumby import AppiumBy

from app_ui.base.base import BasePage


class AddMember(BasePage):
    _NAME = (AppiumBy.XPATH, '//*[contains(@text, "姓名")]/../*[@text="必填"]')
    _PHONE = (AppiumBy.XPATH, '//*[contains(@text, "手机")]/..//*[@text="必填"]')
    _DONTREMIND = (AppiumBy.XPATH, '//*[@text="保存后自动发送邀请通知"]')
    _SAVE = (AppiumBy.XPATH, '//*[@text="保存"]')

    def edit_info(self, name, phone):
        from app_ui.page.addlist_page import AddList
        logging.info("输入姓名")
        self.find_sendkeys(*self._NAME, name)
        logging.info("输入手机")
        self.find_sendkeys(*self._PHONE, phone)
        logging.info("取消选中'保存后自动发送邀请通知'")
        self.find_click(*self._DONTREMIND)
        logging.info("点击保存按钮")
        self.find_click(*self._SAVE)
        logging.info("返回添加成员页面")
        return AddList(self.driver)
