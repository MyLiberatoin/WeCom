'''
@Project ：WeWork 
@File ：test_add_member.py
@Author ：RZ
@Date ：2022/4/2 9:40 PM 
'''
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from faker import Faker


class TestAddMember:
    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "5JP0217715002811",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True
        }
        faker = Faker('zh_CN')
        self.name = faker.name()
        self.phone = faker.phone_number()
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(3)

    def test_add_member(self):
        self.driver.find_element(AppiumBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))').click()
        self.driver.find_element(AppiumBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(AppiumBy.XPATH, '//*[contains(@text, "姓名")]/../*[@text="必填"]').send_keys(self.name)
        self.driver.find_element(AppiumBy.XPATH, '//*[contains(@text, "手机")]/..//*[@text="必填"]').send_keys(self.phone)
        self.driver.find_element(AppiumBy.XPATH, '//*[@text="保存后自动发送邀请通知"]').click()
        self.driver.find_element(AppiumBy.XPATH, '//*[@text="保存"]').click()
        # 获取Toast提示信息
        # while True:
        #     if "添加成功" in self.driver.page_source:
        #         print(self.driver.page_source)
        #         break
        res = self.driver.find_element(AppiumBy.XPATH, '//*[@class="android.widget.Toast"]').get_attribute("text")
        assert res == "添加成功"
