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

            instance.implicitly_wait(0)

            for e in instance._black_list:
                logging.warning(e)
                # 保存原来的上下文
                if instance.driver.context != "NATIVE_APP":
                    instance.save_context()
                    instance.driver.switch_to.context("NATIVE_APP")

                elements = instance.driver.find_elements(*e)
                if len(elements) > 0:
                    elements[0].click()
                    instance.implicitly_wait()

                    # 切换回原来的context
                    instance.restore_context()
                    return magic(*args, **kwargs)

                instance.restore_context()
            instance.implicitly_wait()
            return magic(*args, **kwargs)

    return magic


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _black_list = [
        (By.ID, 'image_cancel'),
        (By.ID, 'tv_agree'),
        (By.XPATH, "//*[@text='下次再说']")
    ]
    _current_context = "NATIVE_APP"
    _retry_max = 1
    _retry = 0
    _default_implicitly_wait_seconds=6
    _default_explicit_wait_seconds = 10

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

    def implicitly_wait(self, seconds=_default_implicitly_wait_seconds):
        self.driver.implicitly_wait(seconds)

    def save_context(self):
        self._current_context = self.driver.context
        if "WEBVIEW" in self._current_context:
            self._current_window = self.driver.current_window_handle

    def restore_context(self):
        if self._current_context != self.driver.context:
            self.driver.switch_to.context(self._current_context)

        if "WEBVIEW" in self._current_context:
            self.driver.switch_to.window(self._current_window)
            logging.info(self.driver.page_source)

    @exception_handle
    def wait(self, locator, timeout=_default_explicit_wait_seconds):
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
        elif isinstance(locator, object):
            logging.info(f"expection_conditions {locator}")
            wait.until(locator)
        else:
            logging.warning(f"don't know how to deal with {locator}")

