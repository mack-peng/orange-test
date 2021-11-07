import core.page_model
from core.page_model import PageModel


class Index(PageModel):

    # 用于覆盖配置的域名
    # _BASE_URL = 'http://news.baidu.com/'

    _URL = '/'

    _XPATH = {
        'null_input': '//*[@id="null"]',
        'search_input': '//*[@id="kw"]',
        'search_btn': '//*[@id="su"]',
    }

    _DATA = {
        'search_input': 'OrangeTest',
    }

    def search(self):
        self.click('null_input')
        self.input('search_input')
        self.click('search_btn')

