#!/usr/bin/python
# coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: action_method.py
@time: 2018/7/22 23:14
"""
from base.base_driver import Base_Driver
from util.get_by_local import Get_By_Local


class ActionMethod:
    '''
	封装selenium操作函数
	'''

    def __init__(self):
        base_driver = Base_Driver()
        driver = self.base_driver.get_driver()

    get_element_local = Get_By_Local()


    def input(self, value):
        '''
        封装操作动作s
        '''
        element = self.get_element_local.get_element()
        if element == None:
           return '元素没找到'
        element.send_keys(value)


    def on_click(self):
        '''
        封装点击操作
        :return:
        '''



    def sleep_time(self):


    # def get_size(self):


    # def get_element(self):
