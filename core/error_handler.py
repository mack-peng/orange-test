import time
import config

# 处理发生错误时，将错误略过
class ErrorHandler:
    debug = config.app['debug']

    def __init__(self, name, desc):
        self._handler(name, desc)

    def _now(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # 错误处理方法
    def _handler(self, name, desc):
        error = "[{0}] 错误：{1}：{2}".format(self._now(), name, desc)
        # 调试模式，抛出错误
        if self.debug:
            raise Exception(error)
        else:
            print(error)

    # 故意将错误发生后的执行集中到此处理
    def __getattr__(self, key):
        def not_find(*args, **kwargs):
            pass
            # print(f'你调用的方法：{key}不存在，参数为：{args}, {kwargs}')
        if key in dir(self):
            return getattr(self, key)
        return not_find
