# TestCLI

基于selenium框架的脚手架，将测试流程变得结构化，工程化

----------------

## 序言

TestCLI是基于selenium框架的脚手架。应对复杂工程的利器，摆脱原有自动化测试代码编写混乱，不好维护的弊病。通过框架，让测试程序开发人员专注于业务逻辑。致力于测试流程模块化，低耦合，多人共同编写维护。互不影响且能统一测试。遵循`Apache2`开源许可协议发布，意味着你可以免费使用TestCLI，甚至允许把你基于TestCLI开发的应用开源或商业产品发布/销售

## 基础

### 安装

**TestCLI**的环境要求如下：

> - Python > 3.7
> - Selenium
> - 谷歌浏览器
> - Chrome Driver

TestCLI无需安装，下载源代码，在以上环境OK的情况下便可运行

#### Git安装

```

项目地址：https://github.com/dnqxj/test-cli

git clone git@github.com:dnqxj/test-cli.git TestCLI
```

#### Chrome Driver 下载

[selenium和chromedriver下载使用](https://www.cnblogs.com/lfri/p/10542797.html)

将下载好的chrome driver放到磁盘某一目录，修改项目根目录下的配置文件（//config.py)。中的app.chrome_path。修改为自己chrome driver的位置。

#### 运行demo

使用python执行根目录下的run.py

### 开发规范

遵循Python开发规范

### 目录结构

project 项目目录

```
├─app           		应用目录
│  ├─controller         控制器目录
│  │  ├─__init__.py     流程控制列表
│  ├─page         		页面目录
│  │─—__init__.py       自动加载逻辑(勿动)
│  │─—main.py       	主流程文件(勿动)
├─autolt                windows脚本
├─core                  核心文件目录
│  ├─BasePage.py        页面操作基类
│  ├─Controller.py      控制器基类
├─config.py             项目配置文件
├─LICENSE.txt           授权说明文件
├─README.md             README 文件
├─run.py                执行入口文件
```

### 配置

主配置文件在项目根目录下的config.py文件

app配置`//config.py`

| 配置参数      | 描述                                                    |
| :------------ | ------------------------------------------------------- |
| base_url      | 项目域名地址                                            |
| initial_path  | 初始化打开地址路径，默认空，打开项目域名                |
| device_name   | 手机端设备配置，eg.iPhone 6/7/8，参照谷歌浏览器设备配置 |
| chrome_path   | chrome driver在电脑中的绝对路径                         |
| window_width  | 窗口的宽度                                              |
| window_height | 窗口的高度                                              |

运行流程配置 `app/controller/__init__.py`

```python
# 这里填写的模块就是执行的顺序，不填写便不执行
__all__ = ['index', 'login', 'search']
```

## 架构

当前框架为单模块应用。后期根据需要是否引入多模块

### 控制器

一个典型的`Index`控制器类如下：

```python
from core.Controller import Controller

# 必须使用修饰器注册controller
@Controller.controller_register('Index')
class Index():
    driver = ''

    def __init__(self, driver):
        self.driver = driver

    # 模块的主运行方法，将自动执行
    def run(self):
        pass
```

### 操作

一个控制器必须包含一个run()方法，该方法运行该控制的主测试逻辑，在程序运行时将自动运行该方法。

下面是一个`run`方法，运行了页面上的输入框输入和按钮点击

```python
from core.Controller import Controller
from app.page.Login import Login as LoginPage

@Controller.controller_register('search')
class Search():
    driver = ''

    # 初始化注入浏览器实例
    def __init__(self, driver):
        self.driver = driver

    # 主测试流程
    def run(self):
        # 使用页面必须传入driver实例
        loginPage = LoginPage(self.driver)
        loginPage.input('search_input')
        loginPage.click('search_btn')

```

### 页面

框架的模型层，框架设计中，对项目的每个页面建立一个实体类，该实体类继承于BasePage。用于便捷的操作页面上元素，与测试逻辑控制层分离。

一个典型的`login`模型类如下：

```python
from core.BasePage import BasePage

# 继承BasePage
class Login(BasePage):
	# 【基本结构】页面路径
    _URL = '/login'
	
    # 【基本结构】页面元素的xpath路径
    _XPATH = {
        'username_input': '//*[@id="TANGRAM__PSP_11__userName"]',
        'password_input': '//*[@id="TANGRAM__PSP_11__password"]',
        'login_btn': '//*[@id="TANGRAM__PSP_11__submit"]',
    }

    # 【基本结构】表单所用数据
    _DATA = {
        'username_input': '******',
        'password_input': '******',
    }
    
    # 复杂页面逻辑可编写方法，供控制器调用，简单的可直接通过控制器操作页面
    def test(self):
        self.input('username_input')
        self.input('password_input')
        self.click('login_btn')


```

一个典型的模型类，必须传递driver实例，用于操作页面元素

```python
 def run(self):
        # 使用页面必须传入driver实例
        loginPage = LoginPage(self.driver)
```



继承与BasePage，包含三个父类方法

- xpath(xpath)：获取页面dom，操作的xpath需要在页面`_XPATH`中定义

- click(xpath)：点击页面上的xpath

- input(self, xpath, data='')：查找元素并填入参数。data为空时会传入定义的同名参数值

  

包含三个数据配置项

- _URL：string，该页面的路径，示例话当前页面模型时，会检查是否为该页面，不是将会跳转到该页面
- _XPATH：{}，定义该页面需要操作的元素的xpath，用于之后方便使用，操作页面都需要在此处定义才能操作  
- _DATA：{}，页面须填写数据定义，使用input(xpath)时，将在此寻找与xpath的同名参数值

### autolt

用于解决上传文件/图片等与操作系统交互的复杂动作自动化

[autolt官网](https://www.autoitscript.com/site/autoit/)

示例：

[python+autoit 实现网页文件上传 - 简书 (jianshu.com)](https://www.jianshu.com/p/007a243bf096)

## 示例

项目自带一个百度搜索的实例，可参照修改

## 问题



## 修改日志

[2021-10-26] 配置文件中添加`initial_path`参数，用于打开项目非域名初始页面



## 联系作者

邮箱：dnqxz@outlook.com



