from core.Controller import Controller

@Controller.controller_register('index')
class index():
    driver = ''

    def __init__(self, driver):
        self.driver = driver

    # 模块的主运行方法，将自动执行
    def run(self):
        pass