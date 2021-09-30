import time


class BasePage:
    base_url = 'http://localhost:8080/#/'
    driver = ''

    def __init__(self, driver, url):
        current_page_url = driver.current_url
        if current_page_url.rfind(url) == -1:
            driver.get(self.base_url + url)
            time.sleep(2)
        # assert currentPageUrl == "https://www.baidu.com/", "当前网页网址非预期！"
        self.driver = driver
