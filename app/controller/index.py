from core.Controller import Controller
from app.page.index import Index as IndexPage

# 使用该修饰对控制器进行注册
@Controller.controller_register('Index')
class Index():
    driver = ''

    def __init__(self, driver):
        self.driver = driver

    # 模块的主运行方法，将自动执行
    def run(self):
        indexPage = IndexPage(self.driver)
        indexPage.search()