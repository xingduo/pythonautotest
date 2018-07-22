#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: get_data.py
@time: 2018/7/14 1:01
"""
from util.opera_excel import Opera_Excel
class GetData:
    def __init__(self):
        # 实例化Excel操作类
        self.opera_Excel = Opera_Excel()
    def get_rows(self):
        '''
        获取Excel行数
        :return: nrows
        '''
        nrows = self.opera_Excel.get_row()
        return nrows
    def get_handle_step(self,row):
        '''
        获取用例里面步骤的操作方法，该方法在表格的第3列
        :param row:
        :return:
        '''
        method_name = self.opera_Excel.get_cell(row,3)
        return method_name
    def get_element_key(self,row):
        '''
        获取操作元素,该元素在表格的第4列
        :return:
        '''
        element_key = self.opera_Excel.get_cell(row,4)
        # 有些情况下，element_key可能为空的情况，需要做一下判断
        if element_key == '':
            return None
        return element_key
    def get_handle_value(self,row):
        '''
         获取操作元素值,该元素在表格的第5列
        :param row:
        :return:
        '''
        element_key = self.opera_Excel.get_cell(row,5)
        # 有些情况下，element_key可能为空的情况，需要做一下判断
        if element_key == '':
            return None
        return element_key
    def get_expect_element(self, row):
        '''
         获取预期值,该元素在表格的第6列
        :param row:
        :return:
        '''
        element_key = self.opera_Excel.get_cell(row, 6)
        # 有些情况下，element_key可能为空的情况，需要做一下判断
        if element_key == '':
            return None
        return element_key
    def get_expect_handle(self, row):
        '''
         获取预期操作,该元素在表格的第7列
        :param row:
        :return:
        '''
        element_key = self.opera_Excel.get_cell(row, 7)
        # 有些情况下，element_key可能为空的情况，需要做一下判断
        if element_key == '':
            return None
        return element_key
    def write_value(self,i,row,value):
        self.opera_Excel.write_value(i,row,value)

