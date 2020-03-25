from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_app.page.base_page import BasePage
from test_app.page.search import SearchPage


class StockSelect(BasePage):
    def clear_all(self):
        all = (By.XPATH, "//*[contains(@resource-id, 'indicator')]//*[@text='全部']")
        #显式等待封装
        self.wait(all)
        self.click(By.ID, 'edit_group')
        if len(self.find_elements(By.ID, "stockName")) > 0:
            self.click(By.XPATH, "//*[@text='全选']")
            self.click(By.XPATH, "//*[@text='取消关注']")
            confirm_buttons = self.find_elements(By.XPATH, "//*[@text='确定']")
            if len(confirm_buttons) > 0:
                confirm_buttons[0].click()
        self.click(By.XPATH, "//*[@text='完成']")

        return self

    def search(self):
        # done
        self.click(By.ID, "action_search")
        return SearchPage(self.driver)

    def select(self, keyword):
        # done:
        self.search().search(keyword).select().cancel()
        return self

    def get_stocks(self):
        # done
        return [element.text for element in self.find_elements(By.ID, "portfolio_stockName")]
