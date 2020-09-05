from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
from logi import Login
import time
import getpages
driver = 0
username = "username"  # Enter your username
password = "password"  # Enter your password
fo = 0


def main():
    global driver
    global fo
    driver = webdriver.Chrome(
        executable_path='driver/chromedriver.exe')
    driver.get('https://www.instagram.com/?hl=en')
    session = Login(driver, username, password)
    session.signin()
    session.check()
    session.profile()
    gp = getpages.GetPage(driver)
    refs = gp.get_followers()
    for r in refs:
        driver.get('https://www.instagram.com' + r)
        time.sleep(3)
        try:
            gp.follow()
            fo += 1
        except:
            print("Something was wrong")

    print(fo)


if __name__ == '__main__':
    main()
