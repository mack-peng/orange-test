import time
import config
from selenium.webdriver.common.keys import Keys

class BasePage:
    base_url = config.app['base_url']
    driver = ''
    _URL = ''
    _XPATH = {}
    _DATA = {}

    def __init__(self, driver):
        url = self._URL
        current_page_url = driver.current_url
        # 该页面的基础utl
        if current_page_url.rfind(url) == -1:
            print(self.base_url + url)
            driver.get(self.base_url + url)
            time.sleep(2)
        # assert currentPageUrl == "https://www.baidu.com/", "当前网页网址非预期！"
        self.driver = driver

    # 封装常用方法
    def xpath(self, xpath):
        if xpath in self._XPATH:
            _xpath = self._XPATH[xpath]
            try:
                ele = self.driver.find_element_by_xpath(_xpath)
                return ele
            except:
                print("错误：元素未找到，key:" + xpath)
                # raise Exception("元素未找到，key:" + xpath)

        else:
            raise Exception("page中未定义该xpath")

    def click(self, xpath):
        self.xpath(xpath).click()
        time.sleep(2)

    # 基本的输入方法
    # xpath:page中定义的_XPATH.key
    # data:page中定义的_DATA.key
    # 如果data不填，那么将使用与xpath同名的_DATA.key
    def input(self, xpath, data=''):
        ele = self.xpath(xpath)
        if data:
            ele.send_keys(self._DATA[data])
        else:
            ele.send_keys(self._DATA[xpath])

    # 选择select，传入两个元素xpath，用于常规select
    def select(self, selectXpath, optionXpath='', _sleep=0.6):
        selectEle = self.xpath(selectXpath)
        selectEle.click()
        time.sleep(_sleep)

        if optionXpath:
            optionEle = self.xpath(optionXpath)
            optionEle.click()

    # 点击元素，向下选择，应对非select下拉框
    def select_down(self, selectXpath, downCount=1, _sleep=0.3):
        selectEle = self.xpath(selectXpath)
        selectEle.click()
        time.sleep(_sleep)
        for i in range(downCount):
            selectEle.send_keys(Keys.DOWN)
        selectEle.send_keys(Keys.ENTER)
