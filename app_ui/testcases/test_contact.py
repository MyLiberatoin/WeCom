'''
@Project ：WeWork 
@File ：test_contact.py
@Author ：RZ
@Date ：2022/4/3 12:11 PM 
'''
import logging

import pytest
import yaml

from app_ui.base.app import App


class TestContact:
    def setup(self):
        self.main = App().start()

    def teardown(self):
        self.main.stop()

    @pytest.mark.parametrize("name, phone, expect", yaml.safe_load(open("../data/member.yaml")))
    def test_contact(self, name, phone, expect):
        logging.info(f"添加成员{name}")
        res = self.main.lauch_main().click_contact().click_addbtn().manual_add().edit_info(name, phone).check_info()
        assert res == expect
