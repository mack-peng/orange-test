from core.data_handler import app_data_handler

class Report:
    """
    框架报告输出类

    用于框架运行完毕后的数据可视化输出
    """

    def __init__(self):
        pass

    def show(self):
        print("===============运行报告=============")
        print("控制器数量：{}".format(app_data_handler.select('controller_num')))
        print("控制器列表：")
        controller_list = app_data_handler.select('controller_list')
        if controller_list != 'None':
            for controller_name in controller_list:
                print(controller_name)
        else:
            print('无')

        print("操作页面数量：{}".format(app_data_handler.select('page_num')))
        print("页面路径列表：")
        page_list = app_data_handler.select('page_list')
        if page_list != 'None':
            for page_name in page_list:
                print(page_name)
        else:
            print('无')

        print('错误数量：{}'.format(app_data_handler.select('error_num')))
        error_list = app_data_handler.select('error_list')
        if error_list != 'None':
            for error_name in error_list:
                print(error_name)
        else:
            print('无')

        print("断言数量：{}".format(app_data_handler.select('equals_num')))
        print("断言失败数量：{}".format(app_data_handler.select('equals_fail_num')))
        print("断言失败列表：")
        equals_fail_list = app_data_handler.select('equals_fail_list')
        if equals_fail_list != 'None':
            for equals_fail in equals_fail_list:
                print(equals_fail)
        else:
            print('无')
