import time
import config
from selenium.webdriver.common.keys import Keys
from core.error_handler import ErrorHandler

class PageModel:
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

    # 私有方法：用于获取xpath，用于错误处理
    def _get_xpath(self, xpath):
        if xpath in self._XPATH:
            return self._XPATH[xpath]
        else:
            return ErrorHandler(xpath, '_XPATH中未定义该属性')

        # 私有方法：用于获取xpath，用于错误处理
    def _get_data(self, data):
        if data in self._DATA:
            return self._DATA[data]
        else:
            return ErrorHandler(data, '_DATA中未定义该属性')

    # xpath获取元素，提前定义到page模型中
    def xpath(self, xpath):
        _xpath = self._get_xpath(xpath)
        # 判断是否为错误处理类的实例
        if not isinstance(_xpath, ErrorHandler):
            try:
                ele = self.driver.find_element_by_xpath(_xpath)
                return ele
            except:
                return ErrorHandler(xpath, '在页面上未找到该元素')
        else:
            return _xpath

    def click(self, xpath):
        self.xpath(xpath).click()
        time.sleep(2)

    # 基本的输入方法
    # xpath:page中定义的_XPATH.key
    # data:填入输入框的数据
    # 如果data不填，那么将使用与xpath同名的_DATA.key
    def input(self, xpath, data=''):
        ele = self.xpath(xpath)
        if data:
            ele.send_keys(data)
        else:
            ele.send_keys(self._get_data(xpath))

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
