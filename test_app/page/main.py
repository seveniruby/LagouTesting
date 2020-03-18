from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_app.page.base_page import BasePage
from test_app.page.search import SearchPage


class MainPage(BasePage):

    def __init__(self):
        caps = {
            "platformName": "android",
            "deviceName": "hogwarts",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "autoGrantPermissions": "true",
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

        WebDriverWait(self.driver, 30).until(lambda x: "同意" in self.driver.page_source)

        # self.find_element(By.ID, "image_cancel").click()
        # self.find_element(By.ID, "tv_agree").click()

    def search(self):
        self.find_element(By.ID, "tv_search").click()
        return SearchPage(self.driver)
