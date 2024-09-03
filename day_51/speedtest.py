from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SpeedTest:
    def __init__(self, url="https://www.speedtest.net/", detach_browser=True):
        self.url = url
        self.driver = self._initialize_driver(detach_browser)
        self.download_speed = None  # To store download speed
        self.upload_speed = None  # To store upload speed

    def _initialize_driver(self, detach_browser):
        chrome_options = webdriver.ChromeOptions()
        if detach_browser:
            chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def run_test(self):
        self.driver.get(self.url)
        self._accept_cookies()
        self._start_test()
        self._get_results()

    def _accept_cookies(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        ).click()

    def _start_test(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "js-start-test"))
        ).click()

    def _get_results(self):
        time.sleep(60)  # Wait for the test to complete
        self.download_speed = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'))
        ).text
        self.upload_speed = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'))
        ).text

    def _print_results(self):
        print(f"Download: {self.download_speed} Mbps")
        print(f"Upload: {self.upload_speed} Mbps")