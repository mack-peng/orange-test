import time
from selenium import webdriver
from app.login.page.LoginPage import LoginPage
from app.mine.page.MinePage import MinePage

class BaseProcess:

    base_url = 'http://localhost:8080/#/'
    device_name = 'iPhone 6/7/8'
    chrome_path = r'D:\Python\chromedriver.exe'

    driver = ''

    def __init__(self):
        driver = self.start_chrome()
        self.driver = driver
        self.driver = self.visitUrl(MinePage.url)

    def visitUrl(self, url):
        targetUrl = self.base_url + url
        self.driver.get(targetUrl)
        time.sleep(1)
        return self.driver

    def start_chrome(self):
        # {'deviceName': '必须与谷歌浏览器的值一致'}
        mobileEmulation = {'deviceName': self.device_name}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)

        driver = webdriver.Chrome(executable_path=self.chrome_path, options=options)
        driver.start_client()
        return driver


    # 集成登录流程
    def loginProcess(self):
        driver = self.driver
        # 获取首页实例
        minePage = MinePage(driver)
        # 调用登录方法
        driver = minePage.jumpLogin()
        # 获取登录页面实例，返回浏览器对象
        loginPage = LoginPage(driver)
        self.driver = loginPage.testLogin()
        # 刷新首页
        driver = self.visitUrl(minePage.url)
        print('登录完成')
        # input()
        return driver



