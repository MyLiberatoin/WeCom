'''
@Project ：WeWork
@File ：test_department.py
@Author ：RZ
@Date ：2022/3/21 9:54 PM
'''
import os
import sys

import allure
import pytest
import yaml
from jsonpath import jsonpath


@allure.feature("通讯录部门管理")
class TestDepartment:
    @allure.story("获取token参数")
    def setup_class(self):
        # 获取token参数
        with allure.step("从yaml文件中读取corpid和corpsecret"):
            with open('../data/config.yaml', 'r') as f:
                datas = yaml.safe_load(f)
                corpid = datas['corpid']
                corpsecret = datas['contact_secret']

        # 实例化Department类
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.append(BASE_DIR)
        from web_api.apis.department import Department
        with allure.step("实例化Department类"):
            self.depart = Department(corpid, corpsecret)
        with allure.step("清除除根部门之外的子部门"):
            self.depart.clear_department()
        self.id = 2

    @allure.story('创建部门')
    def test_create_department(self):
        # 创建部门
        create_data = {
            "name": "吃",
            "name_en": "Eat",
            "parentid": 1,
            "order": 1,
            "id": self.id
        }
        create_res = self.depart.create_department(create_data)
        assert create_res['errcode'] == 0
        id_list = jsonpath(self.depart.get_departments(), "$..id")
        print(id_list)
        assert create_data['id'] in id_list

    @allure.story('更新部门')
    def test_update_department(self):
        # 更新部门信息
        update_data = {
            "id": self.id,
            "name": "吃喝玩乐",
            "name_en": "EDPH"
        }
        update_res = self.depart.update_department(update_data)
        assert update_res['errcode'] == 0
        depart_info = self.depart.get_department_info(self.id)
        assert update_data['name'] == depart_info['department']['name']
        assert update_data['name_en'] == depart_info['department']['name_en']

    @allure.story('删除部门')
    def test_delete_department(self):
        delete_res = self.depart.delete_department(self.id)
        assert delete_res['errcode'] == 0
        id_list = jsonpath(self.depart.get_departments(), "$..id")
        print(id_list)
        assert self.id not in id_list

    @allure.story('获取全部门信息')
    def test_get_department(self):
        # 查询所有部门信息
        depart_list = self.depart.get_departments()
        print(depart_list)
