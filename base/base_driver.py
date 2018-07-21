#coding = utf-8
from appium import webdriver

class Base_Driver:
    '''
    获取设备信息
    '''
    def get_driver(self,deviceName,port):
        '''
        获取driver驱动
        :param driverName:
        :return:driver
        '''

        capabilities = {
            'platformName' : 'Android',
            'deviceName' : deviceName,
            'appPackage' : '',
            'appActivity' : '',
            'app' : '',
            'automationName' : 'appium',
        }
        driver = webdriver.Remote('http://127.0.0.1:'+str(port) + '/wd/hub',capabilities)
        return driver



