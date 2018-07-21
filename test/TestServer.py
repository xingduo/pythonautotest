# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 17:19
# @Author  : 留仙洞
# @FileName: TestServer.py
# @Software: PyCharm
from util.server import Server
import unittest
class TestServer(unittest.TestCase):
    '''
    server的单元测试
    '''
    def test_get_device(self):
        server = Server()
        device_info = server.get_devices()
        print(device_info)