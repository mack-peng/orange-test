class Controller(object):
    _CONTROLLER = {}

    def run(self, driver, controller=()):
        if controller is ():
            for controller_name in self._CONTROLLER.keys():
                driver = self._CONTROLLER[controller_name]().run(driver)
        else:
            for controller_name in controller:
                driver = self._CONTROLLER[controller_name]().run(driver)
        return driver

    @classmethod
    def controller_register(cls, controller_name):
        def wrapper(controller):
            cls._CONTROLLER.update({controller_name: controller})
            return controller
        return wrapper
