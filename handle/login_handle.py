#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: login_handle.py
@time: 2018/7/29 22:01
"""
from page.login_page import LoginPage
class LoginHandle:
    def __init__(self,i):
        self.login_page = LoginPage(i)
    def send_username(self,user):
        self.login_page.get_login_element().send_keys(user)
    def send_password(self,passwrod):
        self.login_page.get_password_element().send_keys(passwrod)
    def check_login(self):
        self.login_page.get_login__button_element().click()

