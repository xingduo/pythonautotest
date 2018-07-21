# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 14:54
# @Author  : 留仙洞
# @FileName: cmd_docs.py
# @Software: PyCharm
import os
class CMD_DOCS:
    '''
    使用cmd命令启动appium
    '''
    def  get_cmd_docs(self,command):
        cmd_list = []
        cmd = os.popen(command).readlines()
        for i in cmd:
            if i == '\n':
                continue
            cmd_list.append(i.strip('\n'))
        return cmd_list
