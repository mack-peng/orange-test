import time
import config

class ErrorHandler:
    """
    错误处理类

    1、格式化显示错误
    2、根据debug配置，决定将错误显示在控制台还是抛出
    3、处理因为错误而阻断的后续程序运行，将错误后的代码执行引入此类，使用__getattr__略过错误
    """
    debug = config.app['debug']

    def __init__(self, name, desc):
        self._handler(name, desc)

    def _now(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def _handler(self, name, desc):
        """
        错误处理逻辑

        :param name: 错误发生的参数或者名称
        :param desc: 错误描述
        :return: debug为False时显示错误在控制台
        :raise: debug为True时抛出错误
        """
        error = "[{0}] 错误：{1}：{2}".format(self._now(), name, desc)
        # 调试模式，抛出错误
        if self.debug:
            raise Exception(error)
        else:
            print(error)

    # 故意将错误发生后的执行集中到此处理
    def __getattr__(self, key):
        """
        处理因为错误而阻断的后续程序运行，将错误后的代码执行引入此类，使用__getattr__略过错误

        :param key:
        :return: 空函数，处理错误后的程序执行
        """
        def not_find(*args, **kwargs):
            pass
            # print(f'你调用的方法：{key}不存在，参数为：{args}, {kwargs}')
        if key in dir(self):
            return getattr(self, key)
        return not_find
