from selenium.webdriver.remote.webdriver import WebDriver


def exception_handle(fun):
    def magic(*args, **kwargs):
        print(f"{fun.__name__} ( {args}, {kwargs})")
        res = fun(*args, **kwargs)
        print(f"{fun.__name__} finish")
        return res

    return magic


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @exception_handle
    def find(self, by, value):
        # todo: 异常处理
        return self.driver.find_element(by, value)

    def close(self):
        self.driver.quit()
