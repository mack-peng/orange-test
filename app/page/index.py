import core.BasePage
from core.BasePage import BasePage


class Index(BasePage):

    _URL = '/'

    _XPATH = {
        'search_input': '//*[@id="kw"]',
        'search_btn': '//*[@id="su"]',
    }

    _DATA = {
        'search_input': 'TestCLI',
    }

    def search(self):
        self.input('search_input')
        self.click('search_btn')

