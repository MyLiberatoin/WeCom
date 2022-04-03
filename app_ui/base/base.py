'''
@Project ：WeWork 
@File ：base.py
@Author ：RZ
@Date ：2022/4/3 12:15 PM 
'''
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_click(self, by, locator):
        return self.find(by, locator).click()

    def find_sendkeys(self, by, locator, words):
        return self.find(by, locator).send_keys(words)

    def scroll_click(self, by, locator, count=3):
        for i in range(count):
            try:
                return self.find_click(by, locator)
            except:
                size = self.driver.get_window_size()
                x = size["width"] / 2
                y_start = size["height"] * 0.8
                y_stop = size["height"] * 0.2
                self.driver.swipe(start_x=x, start_y=y_start, end_x=x, end_y=y_stop, duration=2000)
            if i == count-1:
                raise NoSuchElementException(f"滑动查找了{count}次还是没有找到")
