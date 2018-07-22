#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: opera_excel.py
@time: 2018/7/22 0:35
"""
import xlrd
from xlutils3.copy import copy
import os
class Opera_Excel:
    '''
    Excel表格的操作，包括读和写
    '''
    def __init__(self,file_path=None,i=None):
        #获取当前文件的工作路径：F:\pythonautotest\util
        self.context_path = os.getcwd()
        #获取到当前文件的路径：F:\pythonautotest\util\opera_excel.py
        # file_path = os.path.abspath(__file__)
        #获取当前文件的工作路径：F:\pythonautotest\util
        self.file_path = os.path.dirname(self.context_path)+'\config\case.xls'
        if i == None:
            i=0
        self.excel = self.get_excel()
        self.sheet = self.get_sheet(i)
    def get_excel(self):
        '''
        获取Excel表格
        :return: Excel
        '''
        file_path = self.file_path
        excel = xlrd.open_workbook(file_path)
        return excel

    def get_sheet(self,i):
        '''
        获取sheet
        :param i:
        :return: sheet
        '''
        sheet = self.excel.sheets()[i]
        return sheet
    def get_row(self):
        '''
        获取行数
        :return:
        '''
        nrows = self.sheet.nrows
        return nrows

    def get_cell(self,row,cell):
        '''
        获取单元格内容
        :return:
        '''
        cell = self.sheet.cell(row,cell).value
        return cell
    def write_value(self,i,row,value):
        '''
        对Excel表进行写数据
        :param i:
        :param row:
        :param value:
        :return:
        '''
        read_value = self.excel
        # 将read_value的值复制到内存中 ，这样可以对这些数据进行操作
        write_value = copy(read_value)
        write_sheet = write_value.get_sheet(i)
        # 将数据写到第8列
        write_sheet.write(row,8,value)
        # 将数据存到知道路径的文件夹下
        write_sheet.save(self.file_path)

if __name__ == '__main__':
    o = Opera_Excel()
    print(o.get_excel())
    print(o.get_sheet(0))
    print(o.get_row())
    print(o.get_cell(1,4))
