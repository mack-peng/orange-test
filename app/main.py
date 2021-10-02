import time
import config
from selenium import webdriver
from core.Controller import Controller

class main():

    driver = ''
    base_url = config.app['base_url']
    device_name = config.app['device_name']
    chrome_path = config.app['chrome_path']
    window_width = config.app['window_width']
    window_height = config.app['window_height']

    def __init__(self):
        driver = self.start_chrome()
        self.driver = driver

    def start_chrome(self):
        # {'deviceName': '必须与谷歌浏览器的值一致'}
        options = webdriver.ChromeOptions()
        if self.device_name:
            mobileEmulation = {'deviceName': self.device_name}
            options.add_experimental_option('mobileEmulation', mobileEmulation)

        driver = webdriver.Chrome(executable_path=self.chrome_path, options=options)
        # 设置窗口大小
        driver.set_window_size(self.window_width, self.window_height)
        driver.start_client()
        driver.get(self.base_url)
        return driver

    # 执行所有控制器的run方法
    def run(self):
        controller = Controller()
        controller.run(self.driver)


