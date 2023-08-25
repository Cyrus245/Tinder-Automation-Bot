import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Tinder:
    def __init__(self, driver):
        self.driver = driver

    def clicking_login(self):
        login_btn = WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                '//*[@id="u-1535117240'
                                                                                                '"]/div/div['
                                                                                                '1]/div/main/div['
                                                                                                '1]/div/div/div/div'
                                                                                                '/header/div/div['
                                                                                                '2]/div[2]/a/div['
                                                                                                '2]/div[2]')))

        login_btn.click()

    def login_with_google(self):
        btn = WebDriverWait(driver=self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div[2]/span[1]')))
        btn.click()
        time.sleep(20)

    def login_with_facebook(self, e, p):
        login_with_fb = self.driver.find_element(By.XPATH,

                                                 '//*[@id="u1031468980"]/main/div[1]/div/div[1]/div/div/div[2]/div['
                                                 '2]/span/div[2]/button/div[2]/div[2]/div/div')
        login_with_fb.click()

        # driver.window_handles returns a list of windows handles

        fb_login_window = self.driver.window_handles[1]
        # switching the desired window_handles
        self.driver.switch_to.window(fb_login_window)
        # inputting in the fb window
        email = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        email.send_keys(e)
        password = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        password.send_keys(p)
        login = self.driver.find_element(By.NAME, 'login')
        login.click()

    def login_with_phone(self):
        phone = self.driver.find_element(By.XPATH,
                                         '//*[@id="q-430111019"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div['
                                         '3]/button/div[2]/div[2]/div/div')
        phone.click()

    def accept_cookies(self):
        accept_btn = self.driver.find_element(By.XPATH,
                                              '//*[@id="u-1535117240"]/div/div[2]/div/div/div[1]/div[1]/button/div['
                                              '2]/div[2]')
        accept_btn.click()
