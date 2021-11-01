import core.page_model
from core.page_model import PageModel


class Index(PageModel):

    _URL = '/'

    _XPATH = {
        'null_input': '//*[@id="null"]',
        'search_input': '//*[@id="kw"]',
        'search_btn': '//*[@id="su"]',
    }

    _DATA = {
        'search_input': 'TestCLI',
    }

    def search(self):
        self.click('null_input')
        self.input('search_input')
        self.click('search_btn')

