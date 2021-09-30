import time
from core.Controller import Controller

@Controller.controller_register('login')
class login(object):

    def run(self, driver):
        driver.get('https://blog.csdn.net/')
        time.sleep(2)
        return driver