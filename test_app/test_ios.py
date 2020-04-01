from datetime import datetime

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import hashlib


class TestIOS:
    def setup(self):
        caps = {
            "platformName": "ios",
            "automationName": "xcuitest",
            "deviceName": "iPhone 8 Plus",
            "platformVersion": "13.3",
            "app": "/Users/seveniruby/Library/Developer/Xcode/DerivedData/UICatalog-dmtoqydoakdeeadyqaatomadmnsx/"
                   "Build/Products/Debug-iphonesimulator/UICatalog.app"
        }

        self.driver: WebDriver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 30)

    def test_view(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Alert Views').click()

        text_entry = (MobileBy.ACCESSIBILITY_ID, 'Text Entry')
        self.driver.find_element(*text_entry).click()

        textfield = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')
        self.driver.find_element(*textfield).send_keys("1234")

        cancel_button = (MobileBy.ACCESSIBILITY_ID, 'OK')
        self.driver.find_element(*cancel_button).click()
