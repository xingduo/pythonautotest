#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: run_main.py
@time: 2018/7/14 1:02
"""
from keyword.get_data import GetData
from keyword.action_method import ActionMethod
class RunMain:
    '''
    运行的main类，需要调用的接口有获取驱动类、获取设备类、读取Excel表格数据类、
    页面操作类
    '''
    def run_method(self):
        data = GetData()
        action_method = ActionMethod()
        lines = data.get_rows()
        for i in range(1,lines):
            handle_step = data.get_handle_step(i)
            element_value = data.get_handle_value(i)
            element_key = data.get_element_key(i)
            expect_element = data.get_expect_element(i)
            expect_handle = data.get_expect_handle(i)
            excute_method = getattr(action_method,handle_step)
            if element_key != None:
                excute_method(element_key,element_value)
            else:
                excute_method(element_value)
            if expect_handle != None:
                expect_result = getattr(action_method,expect_handle)
                result = expect_result(expect_element)
                if result:
                    data.write_value(i,'pass')
                else:
                    data.write_value(i,'fail')













