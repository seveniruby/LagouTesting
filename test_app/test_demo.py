# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestDemo:
    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "hogwarts",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "autoGrantPermissions": "true"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

        self.driver.find_element(By.ID, "image_cancel").click()
        self.driver.find_element(By.ID, "tv_agree").click()

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
        size=self.driver.get_window_size()
        print(size)
        sleep(3)
        for i in range(5):
            self.driver.swipe(
                0.5*size['width'], 0.8*size['height'],
                0.5*size['width'], 0.3*size['height'],
                1000
            )




# driver.quit()
