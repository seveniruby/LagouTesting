# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "hogwarts",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "chromedriverExecutableDir": "/Users/seveniruby/projects/chromedriver/chromedrivers",
            "chromedriverChromeMappingFile": "/Users/seveniruby/PycharmProjects/LagouTesting/test_app/chromedriver.json",
            # "chromedriverExecutable": "/Users/seveniruby/projects/chromedriver/chromedrivers/chromedriver_2.20",
            "autoGrantPermissions": "true"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 60)

        locator = ["同意", "image_cancel"]

        def wait_list(driver: WebDriver):
            source = driver.page_source
            return any(map(lambda x: x in source, locator))

        self.wait.until(wait_list)
        self.driver.find_element(By.XPATH, "//*[@text='同意']").click()

    def test_search(self):
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el3.click()
        el4 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el4.send_keys("alibaba")
        el5 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
        el5.click()

    def test_search_new(self):
        self.driver.find_element(By.ID, "tv_search").click()
        self.driver.find_element(By.ID, "search_input_text").send_keys("alibaba")
        self.driver.find_element(By.ID, 'name').click()
        assert float(self.driver.find_element(By.ID, 'current_price').text) > 100

    def test_swipe(self):
        size = self.driver.get_window_size()
        print(size)
        sleep(3)
        for i in range(5):
            self.driver.swipe(
                0.5 * size['width'], 0.8 * size['height'],
                0.5 * size['width'], 0.3 * size['height'],
                1000
            )

    def test_webview(self):
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'tab') and @text='交易']").click()
        # 了解上下文，webview控件如果加载延迟，可以适当的等待
        print(self.driver.contexts)
        # 切换webview上下文
        self.driver.switch_to.context(self.driver.contexts[-1])
        wait=WebDriverWait(self.driver, 10)

        agu=(By.CSS_SELECTOR, 'li.trade_home_agu_3ki')
        wait.until(expected_conditions.visibility_of_element_located(agu))
        # css定位
        self.driver.find_element(*agu).click()
        # 打印窗口列表
        print(self.driver.window_handles)
        # 切换窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone_number = (By.ID, "phone-number")
        # 等待控件可见
        wait.until(expected_conditions.visibility_of_all_elements_located(phone_number))
        self.driver.find_element(*phone_number).send_keys("15600534700")
        self.driver.find_element(By.ID, "code").send_keys("1234")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-submit").click()

# driver.quit()
