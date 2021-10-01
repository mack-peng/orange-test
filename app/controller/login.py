from core.Controller import Controller
from app.page.login import login as LoginPage

@Controller.controller_register('login')
class login():
    # 执行该模块的基本url，如果当前浏览器路径与当前不同，哪么会先执行跳转
    driver = ''

    # 初始化注入浏览器实例
    def __init__(self, driver):
        self.driver = driver

    def run(self):
        loginPage = LoginPage(self.driver)
        loginPage.click('login_model_btn')
        loginPage.input('username')
        loginPage.input('password')
        loginPage.click('login_btn')
        print('执行页面上的图形验证，操作完成后输入任何数据继续...')
        input()

