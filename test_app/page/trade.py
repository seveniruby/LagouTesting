import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_app.page.base_page import BasePage


class TradePage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)

        # 切换webview上下文
        self.wait(lambda x: len(self.driver.contexts) > 1)
        self.driver.switch_to.context(self.driver.contexts[-1])

        def wait_title(driver):
            for handle in self.driver.window_handles:
                self.driver.switch_to.window(handle)
                if "实盘交易" in self.driver.title:
                    return True

        self.wait(wait_title)

    def market_a(self):
        agu = (By.CSS_SELECTOR, 'li.trade_home_agu_3ki')
        self.wait(expected_conditions.visibility_of_element_located(agu))

        count = len(self.driver.window_handles)
        # css定位
        self.click(*agu)
        self.wait(lambda x: len(self.driver.window_handles) > count)
        return self

    def open_account(self, phone, verify_code):
        # 切换窗口

        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone_number = (By.ID, "phone-number")
        # 等待控件可见
        self.wait(expected_conditions.visibility_of_element_located(phone_number))
        self.driver.find_element(*phone_number).send_keys(phone)
        self.driver.find_element(By.ID, "code").send_keys(verify_code)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-submit").click()

    def close(self):
        self.driver.switch_to.context(self.driver.contexts[0])
        self.click(MobileBy.ACCESSIBILITY_ID, "Navigate up")
