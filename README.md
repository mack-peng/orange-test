# test-cli

基于selenium框架的脚手架，将测试流程变得结构化，工程化

## demo介绍
1.down后需要配置chrome_path，在config.py app.chrome_path  
[chromedriver下载使用](https://www.cnblogs.com/lfri/p/10542797.html)
2.执行在run.py  
3.流程  
    3.1、打开baidu.com  
    3.2、登录  
    3.3、手动通过图形验证  
    3.4、搜索框填数据并搜索  

## 框架介绍

|-- autolt 放置window脚本，一般用于上传选择文件  
|-- core 框架核心文件  
|-- app 编写区域  
&nbsp;&nbsp;|-- __init__.py 控制执行时的顺序与需要执行的模块  
&nbsp;&nbsp;|-- controller 业务控制类  
&nbsp;&nbsp;|-- page 页面实体类
main.py 入口文件
config.py 配置文件

##### /app/controller/__init__.py 说明
该文件在添加了控制器后需要在其中添加该控制器模块名，然后依该数组顺序的顺序执行，登录等前置操作放到最前
```python
__all__ = ['index', 'login', 'search']
```

## controller
controller 是框架的控制器层（逻辑层），主要用于跨页面调用逻辑，简单逻辑也可直接写在controller层中
```python
from core.Controller import Controller

# 添加新的controller,需要添加修饰器注册
@Controller.controller_register('search')
class search():
    pass

    driver = ''
    # 添加初始化方法，向类中添加driver实例
    def __init__(self, driver):
        self.driver = driver
    
    # 主逻辑编写函数，run在程序运行时会自动执行
    def run(self):
        pass
```

## page
page 是框架的模型层，框架设计中，对项目的每个页面建立一个实体类，该实体类继承于BasePage，其中有几个默认定义变量  
_URL: string,用于定义该页面的url地址，不带域名前缀。当使用该页面时，如当前浏览器页面不在该页面，将主动跳转到该页面  
_XPATH: {},定义该页面需要操作的元素的xpath，用于之后方便使用，操作页面都需要在此处定义才能操作  
_DATA: {},定义该页面需要填报的数据，用于表单或输入框  

实例化
唯一参数：传入selenium driver浏览器对象  
可使用的方法：  
以下参数xpath都是page实体类中_XPATH中定义的key  
- 封装的父类方法，可直接使用
    - self.xpath(xpath=''): 获取该页面的实体，返回selenium element对象  
    - self.click(xpath): 点击该元素
    - self.input(xpath): 输入元素 

```python
from core.BasePage import BasePage


class login(BasePage):

    _URL = '/'

    _XPATH = {
        'login_model_btn': '//*[@id="s-top-loginbtn"]',
        'search_input': '//*[@id="kw"]',
        'search_btn': '//*[@id="su"]',
        'username': '//*[@id="TANGRAM__PSP_11__userName"]',
        'password': '//*[@id="TANGRAM__PSP_11__password"]',
        'login_btn': '//*[@id="TANGRAM__PSP_11__submit"]',
    }

    _DATA = {
        'search_keyword': '国庆节快乐',
        'username': '****',
        'password': '****',
        'search_input': 'python框架'
    }
    
    # 自定义方法，被控制器所访问。封装页面行为
    def test(self):
        self.click('login_model_btn')
        # 会自动获取 _XPATH中的search_keyword，和填入_DATA中search_keyword的数据
        self.input('search_keyword')
        
```

## config
配置文件

## 使用

控制器目录：/app/controller    
页面： /app/page    
windows脚本：用于操作上传等复杂事务 /autolt    
配置类：config.py    
入口执行文件：run.py 



