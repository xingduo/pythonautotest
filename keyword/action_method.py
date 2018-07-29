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
import time

class ActionMethod:
    '''
	封装selenium操作函数
	'''
    def __init__(self):
        base_driver = Base_Driver()
        self.driver = base_driver.get_driver()
        self.get_element_local = GetByLocal()
        get_size = self.get_size()

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

    def swipe_left(self):
        '''
        封装滑动操作
        :param self:
        :return:
        '''
        x1 = self.get_size()[0]/10*9
        y1 = self.get_size()[1]/2
        x = self.get_size()[0]/10
        # swipe有4个左边参数，数值2000表示坐标移动的时间
        self.driver.swipe(x1,y1,x,y1,2000)
        logging.info('向左滑动')
    def swipe_rigth(self):
        '''
        封装滑动操作
        :param self:
        :return:
        '''
        x1 = self.get_size()[0]/10
        y1 = self.get_size()[1]/2
        x = self.get_size()[0]/10*9
        # swipe有4个左边参数，数值2000表示坐标移动的时间
        self.driver.swipe(x1,y1,x,y1,2000)
        logging.info('向右滑动')
    def swipe_up(self):
        '''
        封装滑动操作
        :param self:
        :return:
        '''
        x = self.get_size()[0]/2
        y1 = self.get_size()[1]/10*6
        y = self.get_size()[1]/10*2
        # swipe有4个左边参数，数值2000表示坐标移动的时间
        self.driver.swipe(x,y1,x,y,2000)
        logging.info('向上滑动')
    def swipe_down(self):
        '''
        封装滑动操作
        :param self:
        :return:
        '''
        x = self.get_size()[0]/2
        y1 = self.get_size()[1]/10
        y = self.get_size()[1]/10*9
        # swipe有4个左边参数，数值2000表示坐标移动的时间
        self.driver.swipe(x,y1,x,y,2000)
        logging.info('向下滑动')

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['heigth']
        return x,y,
    def sleep_time(self,t):
        time.sleep(t)
        logging.info('等待')









