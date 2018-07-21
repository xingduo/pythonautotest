# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 17:01
# @Author  : 留仙洞
# @FileName: server.py
# @Software: PyCharm
from util.cmd_docs import CMD_DOCS
class Server:
    '''
    读取设备信息
    '''

    def get_devices(self):
        docs = CMD_DOCS()  #获取设备信息的cmd
        device_list = docs.get_cmd_docs('adb devices')
        # 'TOIJFQU8R8GMRWI7\tdevice'这是获取到设备后的字符，需要进行整改，取到\t前面的就行
        if len(device_list) > 2 :
            device = device_list[1].split('\t')
            device_info = device[0]
            return device_info
        else:
            return None








