import config
from selenium import webdriver
from core.controller import Controller
from core.data_handler import app_data_handler
from core.data_handler import user_data_handler
from core.report import Report
from core.console import console

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
        console.info("=========OrangeTest========")
        console.info("开始运行~")
        driver = self.start_chrome()
        self.driver = driver

    def start_chrome(self):
        console.info("配置driver~")
        # {'deviceName': '必须与谷歌浏览器的值一致'}
        options = webdriver.ChromeOptions()
        if self.device_name:
            console.info("设置移动端设备~")
            mobileEmulation = {'deviceName': self.device_name}
            options.add_experimental_option('mobileEmulation', mobileEmulation)

        # 添加header
        console.info("添加header头~")
        for header in self.headers:
            options.add_argument("%d=%d".format(header['name'], header['value']))

        driver = webdriver.Chrome(executable_path=self.chrome_path, options=options)

        # 设置窗口大小
        console.info("设置窗口大小，width：{}，height：{}".format(self.window_width, self.window_height))
        driver.set_window_size(self.window_width, self.window_height)
        driver.start_client()

        # 隐式等待10s
        console.info("设置隐式等待时间：{}s".format(self.implicitly_wait))
        driver.implicitly_wait(self.implicitly_wait)
        driver.get(self.base_url + self.initial_path)
        # 添加cookie
        console.info("添加cookie~")
        for cookie in self.cookies:
            driver.add_cookie(cookie)

        return driver

    # 执行所有控制器的run方法
    def run(self):
        # 清空数据库
        console.info("清空数据库~")
        app_data_handler.clear()
        user_data_handler.clear()
        # 运行主测试程序
        console.info("运行主测试程序~")
        controller = Controller()
        controller.run(self.driver)
        # 运行中数据写入文件
        console.info("运行数据写入文件~")
        app_data_handler.write()
        user_data_handler.write()
        console.info("打印报告~")
        report = Report()
        report.show()

