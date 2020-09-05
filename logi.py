from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time


class Login:
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def signin(self):
        uid = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')))
        uid.click()
        uid.send_keys(self.username)

        uid = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input')))
        uid.click()
        uid.send_keys(self.password)

        uid = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button')))
        uid.click()
        time.sleep(5)

    def check(self):
        if EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > div > div > div > button')):
            not_now = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                By.CSS_SELECTOR, '#react-root > section > main > div > div > div > div > button')))
            not_now.click()

        if EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')):
            not_now = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')))
            not_now.click()

    def profile(self):
        # react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(5) > span > img
        move_to_profile = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(5) > span > img')))
        move_to_profile.click()

        move_to_profile = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(5) > div:nth-child(3) > div > div.uo5MA._2ciX.tWgj8.XWrBI > div._01UL2 > a:nth-child(1)')))
        move_to_profile.click()
