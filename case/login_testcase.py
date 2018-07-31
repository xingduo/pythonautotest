#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: login_testcase.py
@time: 2018/7/31 22:49
"""
from base.base_driver import Base_Driver
from business.login_business import LoginBusiness
import HTMLTestRunner
import threading
import logging
import os
import time
import unittest
class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        port = 4723
        device = '127.0.0.1:21503'
        cls.driver = Base_Driver.get_driver(device)
        time.sleep(5)
        cls.login_business = LoginBusiness(cls.driver)

    def setUp(self):
        logging.info('setup')


    def test_Login_Pass(self):
        self.login_business.login_pass()

def get_suite(self,i):
    suite = unittest.TestSuite
    suite.addTest(LoginTestCase('test_Login_Pass',param = i))
    unittest.TextTestRunner().run(suite)
    html_file = os.getcwd()+'\report'+str(i)+'.html'
    fb = open(html_file,'wb')
    HTMLTestRunner.HTMLTestRunner(stream=fb).run(suite)


if __name__ == '__main__':
    thread = []
    for i in range(3):
        t = threading.Thread(target=get_suite,args=(i,))
        thread.append(t)
    for j in thread:
        j.start()
