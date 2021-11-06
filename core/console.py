import time
import config

class Console:
    console_level = config.app['console_level']
    level_num = 2

    level = {
        'info': 1,
        'debug': 2,
        'warning': 3,
        'error': 4,
    }

    def __init__(self):
        self.level_num = self.level[self.console_level]

    def info(self, message=''):
        debug = "[{}] - INFO：{}".format(self._now(), message)
        if self.level_num < 2:
            print(debug)

    def debug(self, message=''):
        debug = "\033[1;36m[{}] - DEBUG：{}\033[0m".format(self._now(), message)
        if self.level_num < 3:
            print(debug)

    def warning(self, message=''):
        debug = "\033[1;33m[{}] - WARNING：{}\033[0m".format(self._now(), message)
        if self.level_num < 4:
            print(debug)

    def error(self, message=''):
        debug = "\033[1;31m[{}] - ERROR：{}\033[0m".format(self._now(), message)
        print(debug)

    def _now(self, message=''):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 实例抛出
console = Console()
