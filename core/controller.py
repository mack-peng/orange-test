from core.data_handler import app_data_handler
from core.console import console

class Controller(object):
    """
    控制器注册与调度运行类

    用于将用户带装饰器的控制器存入列表，在主程序时调用控制器的run方法
    """
    _CONTROLLER = {}

    def run(self, driver, controller=()):
        if controller is ():
            for controller_name in self._CONTROLLER.keys():
                console.info('执行控制器：{}'.format(controller_name))
                app_data_handler.setInc('controller_num')
                app_data_handler.insert_arr('controller_list', controller_name)
                self._CONTROLLER[controller_name](driver).run()
        else:
            for controller_name in controller:
                self._CONTROLLER[controller_name](driver).run()

    @classmethod
    def controller_register(cls, controller_name):

        def wrapper(controller):
            cls._CONTROLLER.update({controller_name: controller})
            return controller
        return wrapper
