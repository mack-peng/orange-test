import time
import config
from selenium import webdriver
from core.controller import Controller
from core.data_handler import DataHandler

# 主运行文件（勿动）
class main():

    driver = ''
    base_url = config.app['base_url']
    initial_path = config.app['initial_path']
    device_name = config.app['device_name']
    chrome_path = config.app['chrome_path']
    window_width = config.app['window_width']
    window_height = config.app['window_height']
    implicitly_wait = config.app['implicitly_wait']
    headers = config.headers
    cookies = config.cookies

    def __init__(self):
        driver = self.start_chrome()
        self.driver = driver

    def start_chrome(self):
        # {'deviceName': '必须与谷歌浏览器的值一致'}
        options = webdriver.ChromeOptions()
        if self.device_name:
            mobileEmulation = {'deviceName': self.device_name}
            options.add_experimental_option('mobileEmulation', mobileEmulation)

        # 添加header
        for header in self.headers:
            options.add_argument("%d=%d".format(header['name'], header['value']))

        driver = webdriver.Chrome(executable_path=self.chrome_path, options=options)

        # 设置窗口大小
        driver.set_window_size(self.window_width, self.window_height)
        driver.start_client()

        # 隐式等待10s
        driver.implicitly_wait(self.implicitly_wait)
        driver.get(self.base_url + self.initial_path)
        # 添加cookie
        for cookie in self.cookies:
            driver.add_cookie(cookie)

        return driver

    # 执行所有控制器的run方法
    def run(self):
        # 清空数据库
        dataHandler = DataHandler()
        dataHandler.clear()
        # 运行主测试程序
        controller = Controller()
        controller.run(self.driver)


