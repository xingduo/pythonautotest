#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: cmd_docsTest.py
@time: 2018/7/21 0:42
"""
import unittest
from util.cmd_docs import CMD_DOCS
class CMD_DOCSTest(unittest.TestCase):
    '''
    对cmd命令行方法的单元测试
    '''
    def test_cmd_docs(self):
        device = '127.0.1'
        port = 4727
        cmd = CMD_DOCS(device,port)
        expect = []
        self.assertEquals(expect,cmd)