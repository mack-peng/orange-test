DEBUG=True

app = {
    'base_url': 'https://www.baidu.com',
    'initial_path': '',
    # 手机端: device_name: iPhone 6/7/8
    'device_name': '',
    'chrome_path': r'D:\Python\chromedriver.exe',
    'window_width': 1299,
    'window_height': 900,
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