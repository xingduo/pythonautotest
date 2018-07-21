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
        '''
        读取系统ccmd内容，需要导入os模块，调用popen（）方法，这里不使用system（），
        因为system（）并没有返回值，没有返回值就意味着不能被其他接口引用，于设计不利。
        '''
        cmd = os.popen(command).readlines()
        for i in cmd:
            if i == '\n':
                continue
            cmd_list.append(i.strip('\n'))
        return cmd_list
