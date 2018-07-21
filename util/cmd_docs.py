#!/usr/bin/python
#coding:utf-8

"""
@author: 留仙洞
@contact: 1451953028@qq.com
@software: PyCharm
@file: cmd_docs.py
@time: 2018/7/19 23:28
"""
import os
class CMD_DOCS:
    '''
    定义使用命令行操作cmd命令
    '''
    def get_cmd(self,device,port):
        cmd = os.popen('appium -a'+ device + 'p'+ str(port)).readlines()
        return cmd
