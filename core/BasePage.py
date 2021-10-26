import time
import config

class BasePage:
    base_url = config.app['base_url']
    driver = ''
    _URL = ''
    _XPATH = {}
    _DATA = {}

    def __init__(self, driver):
        url = self._URL
        current_page_url = driver.current_url
        # 判断当前url与目标页面url是否一致
        if current_page_url.rfind(url) == -1:
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
    # data:自定义输入框数据
    # 如果data不填，那么将使用与xpath同名的_DATA.key
    def input(self, xpath, data=''):
        ele = self.xpath(xpath)
        if data:
            ele.send_keys(data)
        else:
            ele.send_keys(self._DATA[xpath])


