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
from util.get_by_local import GetByLocal
import logging

class ActionMethod:
    '''
	封装selenium操作函数
	'''
    def __init__(self):
        base_driver = Base_Driver()
        self.driver = base_driver.get_driver()
        self.get_element_local = GetByLocal()

    def input(self,row,value):
        '''
        封装操作动作s
        '''
        element = self.get_element_local.get_local_path(row)
        if element == None:
           return logging.info('元素没找到')
        element.send_keys(value)
        logging.info('输入'+ value)

    def on_click(self):
        '''
        封装点击操作
        :return:
        '''
        element = self.get_element_local.get_element()
        if element == None:
            return logging.info('元素没找到')
        element.click()
        logging.info('点击元素'+ element)

    def swipe(self):
        '''
        封装滑动操作
        :param self:
        :return:
        '''

    def get_size(self):
        x = self.driver







