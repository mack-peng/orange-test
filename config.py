# 应用配置
app = {
    # 为True时将抛出错误，False将会略过错误，显示到控制台
    'debug': False,
    # 基础url
    'base_url': 'https://www.baidu.com',
    # 初始化打开url path
    'initial_path': '',
    # 手机端: device_name: iPhone 6/7/8
    'device_name': '',
    # 谷歌driver在磁盘中的位置
    'chrome_path': r'D:\Python\chromedriver.exe',
    # 打开窗口的宽度
    'window_width': 1299,
    # 打开窗口的高度
    'window_height': 900,
    # 隐式等待时间
    'implicitly_wait': 10,
}

# 携带的header
headers = [
    {
        'name': 'Token',
        'value': 'c1ef4ec49c059ec870478a4fc9d8a66d'
    }
]

# 携带的cookie
cookies = [
    {
        'name': 'user',
        'value': 'admin'
    }
]