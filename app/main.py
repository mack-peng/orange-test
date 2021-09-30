import time
from selenium import webdriver
from core.Controller import Controller

def run():

    base_url = 'https://www.baidu.com/'
    device_name = 'iPhone 6/7/8'
    chrome_path = r'D:\Python\chromedriver.exe'

    # mobileEmulation = {'deviceName': device_name}
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('mobileEmulation', mobileEmulation)

    # driver = webdriver.Chrome(executable_path=chrome_path, options=options)
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.set_window_size(1000, 900)
    driver.start_client()
    driver.get(base_url)
    time.sleep(4)
    # 执行所有控制器的run方法
    controller = Controller()
    controller.run(driver)
