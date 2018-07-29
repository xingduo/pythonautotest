#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: login_business.py
@time: 2018/7/29 22:01
"""
from handle.login_handle import LoginHandle
class LoginBusiness:
    def __init__(self,i):
        self.login_handle = LoginHandle(i)

    def login_pass(self):
        self.login_handle.send_username()
        self.login_handle.send_password()
        self.login_handle.check_login()




