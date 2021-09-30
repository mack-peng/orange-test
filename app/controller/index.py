import time
from core.Controller import Controller

@Controller.controller_register('index')
class index(object):
    url = '/'

    def run(self, driver):
        driver.get('https://www.qq.com')
        time.sleep(2)
        return driver