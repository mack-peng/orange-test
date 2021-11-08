import time
import random
import config
from selenium.webdriver.common.keys import Keys
from core.error_handler import ErrorHandler
from core.data_handler import app_data_handler
from core.console import console

class PageModel:
    """
    页面模型基类

    用于便捷的操作页面元素，和处理错误
    注：页面上所有xpath参数，表示的都是页面模型中_XPATH字典定义的名称。不能直接传入xpath路径
    """
    driver = ''
    _BASE_URL = config.app['base_url']
    _URL = ''
    _XPATH = {}
    _DATA = {}

    def __init__(self, driver):
        url = self._BASE_URL + self._URL
        console.info('运行页面模型：{}'.format(url))
        app_data_handler.setInc("page_num")
        app_data_handler.insert_arr("page_list", url)
        current_page_url = driver.current_url
        if current_page_url.rfind(url) == -1:
            driver.get(url)
            time.sleep(2)
        current_page_url = driver.current_url
        if current_page_url.rfind(url) == -1:
            console.warning("{} : {}".format(url, '未切换到目标页面'))
        self.driver = driver

    def xpath(self, xpath):
        """
        获取页面上的元素dom实例

        :param xpath: 定义在页面模型中的_XPATH中的名称
        :return: 页面dom实例
        :raise: 正常返回ErrorHandler实例，该实例解决在可能的错误的dom获取下，不影响后面的程序执行
        """
        _xpath = self._get_xpath(xpath)
        if not isinstance(_xpath, ErrorHandler):
            try:
                ele = self.driver.find_element_by_xpath(_xpath)
                return ele
            except:
                return ErrorHandler(xpath, '在页面上未找到该元素')
        else:
            return _xpath


    def click(self, xpath, _sleep=2):
        """
        点击页面上的元素

        :param xpath:要点击元素的xpath
        :param _sleep:点击后的间隔时间，默认2s
        :return:
        """
        self.xpath(xpath).click()
        time.sleep(_sleep)


    def input(self, xpath, data=''):
        """
        输入框表单项填入数据

        :param xpath: 操作的输入框xpath名
        :param data:为空时，将在_DATA中寻找xpath名相同的值
        :return:
        """
        ele = self.xpath(xpath)
        if data:
            ele.send_keys(data)
        else:
            ele.send_keys(self._get_data(xpath))

    def input_random(self, xpath, num=5, prefix=''):
        """
        向页面输入框元素填入随机字符串

        :param xpath: 输入元素的xpath
        :param num: 随机字符串的长度，默认5
        :param prefix: 随机字符串前缀，默认空
        :return: void
        """
        ele = self.xpath(xpath)
        data = self._ranstr(num, prefix)
        ele.send_keys(data)

    # 选择select，传入两个元素xpath，用于常规select
    def select(self, selectXpath, optionXpath='', _sleep=0.6):
        """
        用于常规的select

        :param selectXpath: 下拉元素xpath
        :param optionXpath: 选项元素xpath
        :param _sleep: 等待下拉弹出的间隔时间，默认0.6s
        :return:
        """
        selectEle = self.xpath(selectXpath)
        selectEle.click()
        time.sleep(_sleep)

        if optionXpath:
            optionEle = self.xpath(optionXpath)
            optionEle.click()


    def select_down(self, selectXpath, downCount=1, _sleep=0.3):
        """
        处理非select下拉的方法，点击下拉元素，向下选择option，并确认

        :param selectXpath: 将操作的下拉元素xpath
        :param downCount: 向下选择个数，默认1
        :param _sleep: 点击下拉元素后的等待时间，默认0.3s
        :return:
        """
        selectEle = self.xpath(selectXpath)
        selectEle.click()
        time.sleep(_sleep)
        for i in range(downCount):
            selectEle.send_keys(Keys.DOWN)
        selectEle.send_keys(Keys.ENTER)

    def equals_xpath_exist(self, xpath):
        """
        断言元素页面是否定义

        :param xpath: 元素的xpath
        :return: Boolean True：页面上存在，False：页面上不存在
        """
        ele = self.xpath(xpath)
        app_data_handler.setInc("equals_num")
        if isinstance(ele, ErrorHandler):
            fail_mesage = '断言 - {} - 元素页面是否定义 - 失败'.format(xpath)
            app_data_handler.setInc("equals_fail_num")
            app_data_handler.insert_arr("equals_fail_list", fail_mesage)
            console.warning(fail_mesage)
            return False
        else:
            console.info('断言 - {} - 元素页面是否定义 - 成功'.format(xpath))
            return True

    def equals_xpath_text(self, xpath, text=''):
        """
        断言元素文字是否符合预期

        :param xpath:元素的xpath
        :param text:预期的字符串
        :return:Boolean True: 符合预期，False：不符合预期
        """
        ele = self.xpath(xpath)
        content = ele.get_attribute("textContent")
        app_data_handler.setInc("equals_num")
        if content == text:
            console.info('断言 - {} - 元素的值为 {} - 成功 '.format(xpath, text))
            return True
        else:
            fail_mesage = '断言 - {} - 元素的值为 {} - 失败 '.format(xpath, text)
            app_data_handler.setInc("equals_fail_num")
            app_data_handler.insert_arr("equals_fail_list", fail_mesage)
            console.warning(fail_mesage)
            return False

    def equals_current_url(self, url=''):
        """
        断言当前页面url是否是预期url，可传入全部或部分url

        :param url: 全部或部分url
        :return:Boolean True: 符合预期，False：不符合预期
        """
        current_page_url = self.driver.current_url
        app_data_handler.setInc("equals_num")
        if current_page_url.rfind(url) == -1:
            fail_mesage = '断言 - 浏览器地址包含 {} - 失败 '.format(url)
            app_data_handler.setInc("equals_fail_num")
            app_data_handler.insert_arr("equals_fail_list", fail_mesage)
            console.warning(fail_mesage)
            return False
        else:
            console.info('断言 - 浏览器地址包含 {} - 成功 '.format(url))
            return True

    def _ranstr(self, num=5, prefix=''):
        """
        生成随机字符串

        :param num: 随机字符串长度
        :param prefix: 随机字符串前缀
        :return: 随机字符串
        """
        H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        salt = ''
        for i in range(num):
            salt += random.choice(H)
        salt = prefix + salt
        return salt


    def _get_xpath(self, xpath):
        """
        获取定义在页面模型中_XPATH中的xpath路径

        :param xpath: _XPATH中的字典名称
        :return: 该字典对应的值
        :return: 发生错误时，返回错误处理实例
        """
        if xpath in self._XPATH:
            return self._XPATH[xpath]
        else:
            return ErrorHandler(xpath, '_XPATH中未定义该属性')

    def _get_data(self, data):
        """
        获取定义在页面模型中_DATA中的数据

        :param data: _DATA中的字典名称
        :return: 该字典对应的值
        :return: 发生错误时，返回错误处理实例
        """
        if data in self._DATA:
            return self._DATA[data]
        else:
            return ErrorHandler(data, '_DATA中未定义该属性')


