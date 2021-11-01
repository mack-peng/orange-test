class Controller(object):
    _CONTROLLER = {}

    def run(self, driver, controller=()):
        if controller is ():
            for controller_name in self._CONTROLLER.keys():
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
