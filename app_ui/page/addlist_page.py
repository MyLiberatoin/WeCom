'''
@Project ：WeWork 
@File ：addlist_page.py
@Author ：RZ
@Date ：2022/4/3 12:14 PM 
'''
import logging

from appium.webdriver.common.appiumby import AppiumBy

from app_ui.base.base import BasePage


class AddList(BasePage):
    _MANUAL_CLICK = (AppiumBy.XPATH, '//*[@text="手动输入添加"]')
    _TOAST = (AppiumBy.XPATH, '//*[@class="android.widget.Toast"]')

    def manual_add(self):
        from app_ui.page.addmember_page import AddMember
        logging.info("点击手动输入添加")
        self.find_click(*self._MANUAL_CLICK)
        logging.info("跳转到编辑添加成员页面")
        return AddMember(self.driver)

    def check_info(self):
        logging.info("获取添加后的提示信息")
        toast = self.find(*self._TOAST).get_attribute("text")
        return toast
