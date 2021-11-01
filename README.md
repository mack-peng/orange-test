# TestCLI

基于 selenium 框架的脚手架，将测试流程变得结构化，工程化

---

## 序言

TestCLI 是基于 selenium 框架的脚手架。应对复杂工程的利器，摆脱原有自动化测试代码编写混乱，不好维护的弊病。通过框架，让测试程序开发人员专注于业务逻辑。致力于测试流程模块化，低耦合，多人共同编写维护。互不影响且能统一测试。遵循`Apache2`开源许可协议发布，意味着你可以免费使用 TestCLI，甚至允许把你基于 TestCLI 开发的应用开源或商业产品发布/销售

## 基础

### 安装

**TestCLI**的环境要求如下：

> - Python3
> - Selenium
> - 谷歌浏览器
> - Chrome Driver

TestCLI 无需安装，下载源代码，在以上环境 OK 的情况下便可运行

#### Git 安装

```

项目地址：https://github.com/dnqxj/test-cli

git clone git@github.com:dnqxj/test-cli.git TestCLI
```

#### Chrome Driver 下载

[selenium 和 chromedriver 下载使用](https://www.cnblogs.com/lfri/p/10542797.html)

将下载好的 chrome driver 放到磁盘某一目录，修改项目根目录下的配置文件（//config.py)。中的 app.chrome_path。修改为自己 chrome driver 的位置。

#### 运行 demo

使用 python 执行根目录下的 run.py

### 开发规范

命名遵循 Python 开发规范

开发时，用户仅需关注`controller`和`page`目录文件即可

### 目录结构

project 项目目录

```
├─app           		应用目录
│  ├─controller         控制器目录
│  │  ├─__init__.py     流程控制列表
│  ├─page         		页面目录
│  ├─__init__.py        自动加载逻辑(勿动)
│  ├─main.py       	    主流程文件(勿动)
├─autolt                windows脚本
├─core                  核心文件目录
│  ├─page_model.py      页面操作基类
│  ├─controller.py      控制器基类
│  ├─error_handler.py   错误处理类
├─config.py             项目配置文件
├─LICENSE.txt           授权说明文件
├─README.md             README 文件
├─run.py                执行入口文件
```

### 配置

主配置文件在项目根目录下的 config.py 文件

app 配置`//config.py`

| 配置参数      | 描述                                                    |
| :------------ | ------------------------------------------------------- |
| debug         | 为True时将抛出错误，False将会略过错误，显示到控制台     |
| base_url      | 项目域名地址                                            |
| initial_path  | 初始化打开地址路径，默认空，打开项目域名                |
| device_name   | 手机端设备配置，eg.iPhone 6/7/8，参照谷歌浏览器设备配置 |
| chrome_path   | chrome driver 在电脑中的绝对路径                        |
| window_width  | 窗口的宽度                                              |
| window_height | 窗口的高度                                              |

header 配置//config.py

对象列表方式配置

```python
headers = [
    {
        'name': 'Token',
        'value': 'c1ef4ec49c059ec870478a4fc9d8a66d'
    }
]
```

cookie配置//config.py

对象列表方式配置

```python
cookies = [
    {
        'name': 'user',
        'value': 'admin'
    }
]
```

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
from core.controller import Controller


# 使用修饰器注册控制器
@Controller.controller_register('Index')
class Index():
    driver = ''

    # 初始化注入浏览器实例
    def __init__(self, driver):
        self.driver = driver

    # 模块的主运行方法，将自动执行
    def run(self):
        pass
```

### 操作

一个控制器必须包含一个`run()`方法，该方法是控制器的主测试流程，在程序运行时将自动运行该方法。

下面是一个`run()`方法，运行了`LoginPage`页面上的输入框输入和按钮点击

```python
from core.controller import Controller
from app.page.Login import Login as LoginPage


# 使用修饰器注册控制器
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

框架的模型层，框架设计中，对项目的每个页面建立一个实体类，该实体类继承于 PageModel。用于便捷的操作页面上元素，与测试逻辑控制层分离。

一个典型的`login`模型类如下：

```python
from core.page_model import PageModel


# 继承PageModel
class Login(PageModel):
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

使用页面模型时，必须传递 driver 实例，用于操作页面元素

```python
 def run(self):
     # 使用页面必须传入driver实例
     loginPage = LoginPage(self.driver)
```

页面模型继承于`PageModel`，包含以下父类方法，传递的 xpath 都为在模型中定义的\_XPATH 对象名称

- xpath(xpath)：获取页面 dom

- click(xpath)：点击该 xpath 元素

- input(xpath, data='')：查找元素并填入参数。data 为空时会传入\_DATA 中定义的同名对象值

- select(selectXpath, optionXpath, \_sleep=0.6)：点击页面下拉方法，传入两个 xpath。间隔时间默认 0.6s

- select_down(selectXpath, downCount=1, \_sleep=0.3)：用于处理非 select 下拉选项，传入下拉元素的 xpath 即可，downCount：选择第几项。默认延时0.3s

包含三个数据配置项

- \_URL：string，该页面的路径，实例化该页面模型时，会检查是否为该页面，不是将会跳转到该页面
- \_XPATH：{}，定义该页面需要操作的元素的 xpath，用于之后方便使用，操作页面都需要在此处定义才能操作
- \_DATA：{}，表单填写数据定义，使用 input(xpath)时，将在此寻找与 xpath 的同名对象参数值

### 错误处理

框架的错误处理类，文件在`core/error_handler`。用于格式化显示错误。配置`app.debug`为True时，将抛出错误。为False时将略过错误。将错误显示在控制台

### autolt

用于解决上传文件/图片等与操作系统交互的复杂动作自动化

[autolt 官网](https://www.autoitscript.com/site/autoit/)

示例：

[python+autoit 实现网页文件上传 - 简书 (jianshu.com)](https://www.jianshu.com/p/007a243bf096)

## 示例

项目自带一个百度搜索的实例，可参照修改

## 问题

一、核心文件与开发目录混杂，初学者会有困惑。关注控制器和模型层即可

二、错误处理和生成测试报告



## 更新日志

[2021-10-26] 配置文件中添加`initial_path`参数，用于打开项目非域名初始页面

[2021-11-01] 配置文件中添加`header`，`cookies`配置，项目运行时将携带

[2021-11-01] 新增主程序隐式等待配置，默认 10s，可配置(app.implicitly_wait)

[2021-11-01] 配置文件中添加`header`，`cookies`配置，项目运行时将携带

[2021-11-01] 页面模型基类新增`select_down`方法，用于处理非 select 下拉选择

[2021-11-02] 添加框架错误处理类ErrorHandler。用于处理框架中抛出的错误

[2021-11-02] 新增app.debug配置。用于配置是否为调试模式。涉及到错误处理

## 联系作者

邮箱：dnqxz@outlook.com
