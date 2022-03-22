'''
@Project ：WeWork
@File ：department.py
@Author ：RZ
@Date ：2022/3/21 9:48 PM
'''
import allure
from jsonpath import jsonpath

from web_api.apis.wework import WeWork


class Department(WeWork):
    def create_department(self, data):
        req = {
            "method": "POST",
            "url": f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}',
            "json": data
        }
        r = self.send_api(req)
        return r.json()

    def update_department(self, data):
        req = {
            "method": "POST",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}",
            "json": data
        }
        r = self.send_api(req)
        return r.json()

    def delete_department(self, id):
        req = {
            "method": "GET",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={id}"
        }
        r = self.send_api(req)
        return r.json()

    def get_departments(self):
        req = {
            "method": 'GET',
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        }
        r = self.send_api(req)
        return r.json()

    def get_department_children(self, id):
        req = {
            "method": "GET",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/simplelist?access_token={self.token}&id={id}"
        }
        r = self.send_api(req)
        return r.json()

    def get_department_info(self, id):
        req = {
            "method": "GET",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/get?access_token={self.token}&id={id}"
        }
        r = self.send_api(req)
        return r.json()

    def clear_department(self):
        departs = self.get_departments()
        id_list = jsonpath(departs, "$..id")

        for id in id_list:
            depart = self.get_department_children(id)
            # 不能删除根部门
            if id == 1:
                continue
            # 删除没有子部门的部门
            elif len(depart['department_id']) == 1:
                with allure.step(f"删除部门：{self.get_department_info(id)['department']['name']}"):
                    self.delete_department(id)
            # 不能直接删除含有子部门的部门, 将子部门删除后再删除父部门
            elif len(depart['department_id']) > 1:
                parent_id = depart['department_id'][0]['id']
                parent_name = self.get_department_info(parent_id)['department']['name']
                for de in depart['department_id']:
                    if de['id'] != parent_id:
                        child_id = de['id']
                        child_name = self.get_department_info(child_id)['department']['name']
                        with allure.step(f"删除子部门：{child_name}"):
                            self.delete_department(child_id)
                with allure.step(f"删除父部门：{parent_name}"):
                    self.delete_department(parent_id)
