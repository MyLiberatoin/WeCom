'''
@Project ：WeWork
@File ：test_department.py
@Author ：RZ
@Date ：2022/3/21 9:54 PM
'''
import os
import sys

import allure
import yaml
from jsonpath import jsonpath
from web_api.apis.department import Department


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
        with allure.step("实例化Department类"):
            self.depart = Department(corpid, corpsecret)
        with allure.step("清除除根部门之外的子部门"):
            self.depart.clear_department()
        self.id = 2

    @allure.story('创建部门')
    def test_create_department(self):
        # 创建部门
        create_data = {
            "name": "技术部",
            "name_en": "Technology",
            "parentid": 1,
            "order": 1,
            "id": self.id
        }
        with allure.step("创建<技术部>"):
            create_res = self.depart.create_department(create_data)
        with allure.step("根据返回结果断言<技术部>创建成功"):
            assert create_res['errcode'] == 0
        with allure.step("根据部门列表断言<技术部>创建成功"):
            id_list = jsonpath(self.depart.get_departments(), "$..id")
            print(id_list)
            assert create_data['id'] in id_list

    @allure.story('更新部门')
    def test_update_department(self):
        # 更新部门信息
        update_data = {
            "id": self.id,
            "name": "技术分享部",
            "name_en": "Technology-Sharing"
        }
        with allure.step("修改<技术部>为<技术分享部>"):
            update_res = self.depart.update_department(update_data)
        with allure.step("根据返回结果断言<技术分享部>修改成功"):
            assert update_res['errcode'] == 0
        with allure.step("根据部门信息断言<技术分享部>修改成功"):
            depart_info = self.depart.get_department_info(self.id)
            assert update_data['name'] == depart_info['department']['name']
            assert update_data['name_en'] == depart_info['department']['name_en']

    @allure.story('删除部门')
    def test_delete_department(self):
        with allure.step("删除<技术分享部>"):
            delete_res = self.depart.delete_department(self.id)
        with allure.step("根据返回结果断言<技术分享部>删除成功"):
            assert delete_res['errcode'] == 0
        with allure.step("根据部门列表断言<技术分享部>删除成功"):
            id_list = jsonpath(self.depart.get_departments(), "$..id")
            print(id_list)
            assert self.id not in id_list

    @allure.story('获取全部门信息')
    def test_get_department(self):
        # 查询所有部门信息
        with allure.step("获取所有部门信息"):
            depart_list = self.depart.get_departments()
            print(depart_list)
