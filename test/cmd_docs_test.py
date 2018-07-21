# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 15:23
# @Author  : 留仙洞
# @FileName: cmd_docs_test.py
# @Software: PyCharm
import unittest
from util.cmd_docs import CMD_DOCS
class Test_CMD_DOCS(unittest.TestCase):
    docs = CMD_DOCS()
    cmd = docs.get_cmd_docs('adb devices')
    print (cmd)
