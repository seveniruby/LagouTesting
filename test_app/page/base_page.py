from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _black_list=[
        (By.ID, 'image_cancel'),
        (By.ID, 'tv_agree')
    ]
    def __init__(self):
        self.driver: WebDriver = None

    def find_element(self, by, value):
        #todo: 异常处理, 退出条件
        try:
            element=self.driver.find_element(by, value)
            return element
        except Exception as e:
            for e in self._black_list:
                elements=self.driver.find_elements(*e)
                if len(elements)>0:
                    elements[0].click()
            return self.find_element(by, value)

