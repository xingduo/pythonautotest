# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 15:48
# @Author  : 留仙洞
# @FileName: get_by_local.py
# @Software: PyCharm
from util.opera_excel import Opera_Excel
class GetByLocal:

    def __init__(self, driver):
        self.driver = driver
        self.opera_excel = Opera_Excel()

    def get_local_path(self,row):
        by = self.opera_excel.get_cell(row,4)
        local_by = self.opera_excel.get_cell(row,5)
        if by == 'id':
            return self.driver.find_element_by_id(local_by)
        elif by == 'class_name':
            return self.driver.find_element_by_classname(local_by)
        elif by == 'xpath':
            return self.driver.find_element_by_xpath(local_by)
        else:
            return self.driver.find_element_by_xpath(local_by)







        
