# -*- coding: UTF-8 -*-
'''
@Project ：WeWork
@File ：test_po_add_member.py
@Author ：RZ
@Date ：2022/3/14 11:41 AM
'''
import logging
import os.path
import sys
import allure
import pytest
from faker import Faker


@allure.story('生成随机数据')
def faker_data():
    # 使用faker造数据: 名字，身份证，电话号码
    faker = Faker('zh_CN')
    data = []
    with allure.step('生成3条数据'):
        for i in range(3):
            data.append([faker.name(), faker.ssn(), faker.phone_number()])
    logging.info('使用faker造数据')
    return data


@allure.feature('执行测试')
class TestAddMember:

    def setup(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.append(BASE_DIR)
        from web_ui.page_objects.main_page import MainPage
        self.main_page = MainPage()
        logging.info('实例化首页')

    def teardown(self):
        # pass
        self.main_page.driver.quit()
        logging.info('关闭浏览器')

    @pytest.mark.parametrize('name, acctid, mobile_phone', faker_data())
    def test_add_member(self, name, acctid, mobile_phone):
        logging.info('开始测试企业微信添加成员功能')
        # 链式调用
        with allure.step('链式调用'):
            # 在首页点击添加成员
            # names = self.main_page.click_add_btn().fill_info(name, acctid, mobile_phone).check_info()
            # 在通讯录页点击添加成员
            names = self.main_page.go_to_contact().click_add_btn().fill_info(name, acctid, mobile_phone).check_info()
            logging.info('链式调用')
        with allure.step('断言添加的成员姓名是否在通讯录所有成员姓名列表中'):
            assert name in names
            logging.info(f'断言 {name} 在 {names} 成员列表中')
