import logging

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def exception_handle(fun):
    def magic(*args, **kwargs):
        instance: BasePage = args[0]
        try:
            logging.info(f"{fun.__name__} {args[1:]} {kwargs}")
            result = fun(*args, **kwargs)
            instance._retry = 0
            return result
        except Exception as e:
            instance._retry += 1
            logging.warning("exception handle")
            if instance._retry > instance._retry_max:
                raise e

            instance.driver.implicitly_wait(0)
            for e in instance._black_list:
                logging.warning(e)
                elements = instance.driver.find_elements(*e)
                if len(elements) > 0:
                    elements[0].click()
                    instance.driver.implicitly_wait(10)
                    return magic(*args, **kwargs)
            instance.driver.implicitly_wait(10)
            return magic(*args, **kwargs)

    return magic


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _black_list = [
        (By.ID, 'image_cancel'),
        (By.ID, 'tv_agree'),
        (By.XPATH, "//*[@text='下次再说']")
    ]
    _retry_max = 1
    _retry = 0

    def __init__(self, driver=None):
        self.driver: WebDriver = driver

    @exception_handle
    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    @exception_handle
    def click(self, by, value):
        self.driver.find_element(by, value).click()

    @exception_handle
    def wait(self, locator, timeout=20):
        wait = WebDriverWait(self.driver, timeout)
        if isinstance(locator, tuple):
            wait.until(
                lambda x: len(self.driver.find_elements(*locator)) > 0
            )
        elif isinstance(locator, str):
            wait.until(lambda x: locator in self.driver.page_source)
        elif isinstance(locator, list):
            def wait_list(driver: WebDriver):
                source = driver.page_source
                return any(map(lambda x: x in source, locator))

            wait.until(wait_list)
        else:
            logging.warning(f"don't know how to deal with {locator}")
