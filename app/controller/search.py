from core.Controller import Controller
from app.page.login import login as LoginPage

@Controller.controller_register('search')
class search():
    driver = ''

    # 初始化注入浏览器实例
    def __init__(self, driver):
        self.driver = driver

    # 作为主测试流程，跑整个模块
    def run(self):
        loginPage = LoginPage(self.driver)
        loginPage.input('search_input')
        loginPage.click('search_btn')
