# -*- coding: UTF-8 -*-
'''
@Project ：WeWork
@File ：conftest.py
@Author ：RZ
@Date ：2022/3/14 7:47 PM
'''


def pytest_collection_modifyitems(session, config, items: list):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
