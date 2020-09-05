from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time


class GetPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.instagram.com/instagram/')
        self.hrefs = []

    def get_followers(self):
        time.sleep(2)
        click_flw_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')))
        click_flw_btn.click()
        self.popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div.isgrP')))
        for h in range(30):
            time.sleep(2)
            print('scrolling')
            print(h)
            print(
                'arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11 - h)))
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11 - h)), self.popup)
            if h == 5:
                break
        for i in range(40):
            time.sleep(2)
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollHeight', self.popup)

        self.popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div.isgrP')))
        b_popup = b(self.popup.get_attribute('innerHTML'), 'html.parser')
        # print(b_popup.prettify())
        print(len(b_popup.findAll('li', {'class': 'wo9IH'})))
        for p in b_popup.findAll('li', {'class': 'wo9IH'}):
            try:
                print(p.findAll('a')[0]['href'])
                hlinks = p.findAll('a')[0]['href']
                self.hrefs.append(hlinks)
            except:
                print("Could not append")

        print(self.hrefs)
        return self.hrefs

    def follow(self):
        time.sleep(1)
        follow_button = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/span/span[1]/button')))
        f_text = follow_button.text
        if f_text.lower() == 'follow' or f_text.lower() == 'follow back':
            follow_button.click()
        else:
            print("already following")
