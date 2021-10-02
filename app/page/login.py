import core.BasePage
from core.BasePage import BasePage


class login(BasePage):

    _URL = '/'

    _XPATH = {
        'login_model_btn': '//*[@id="s-top-loginbtn"]',
        'search_input': '//*[@id="kw"]',
        'search_btn': '//*[@id="su"]',
        'username': '//*[@id="TANGRAM__PSP_11__userName"]',
        'password': '//*[@id="TANGRAM__PSP_11__password"]',
        'login_btn': '//*[@id="TANGRAM__PSP_11__submit"]',
    }

    _DATA = {
        'search_keyword': '国庆节快乐',
        'username': '17683278861',
        'password': 'hepeng123',
        'search_input': 'python框架'
    }

