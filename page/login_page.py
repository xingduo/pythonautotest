#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: login_page.py
@time: 2018/7/29 22:02
"""
from util.get_by_local import GetByLocal
from util.opera_excel import Opera_Excel
from base.base_driver import Base_Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    def __init__(self):
        self.driver = Base_Driver().get_driver()
        self.get_by_local = GetByLocal(self.driver)
    def get_login_element(self,row=2):
        return self.get_by_local.get_local_path(row)

    def get_password_element(self,row=3):
        return self.get_by_local.get_local_path(row)
    def get_login__button_element(self,row=4):
        return self.get_by_local.get_local_path(row)
    def get_forget_password_element(self,row=5):
        return self.get_by_local.get_local_path(row)
    def get_register_element(self,row=6):
        return self.get_by_local.get_local_path(row)




