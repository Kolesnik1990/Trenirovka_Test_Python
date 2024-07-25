# -*- coding: utf8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--window-size=1920,1080")

browser.get("https://ya.ru/")
browser.maximize_window()
wait = WebDriverWait(browser, 15)


SEARCH = ("xpath", "//input[@class='search3__input mini-suggest__input']")
FIND = ("xpath", "//button[text()='Найти']")
YANDEX = ("xpath", "//a[@class='_market-feed-d218c _market-feed-77dc5']")


wait.until(EC.visibility_of_element_located(SEARCH)).send_keys("Hello Word")
browser.find_element(*FIND).click()
browser.back()

browser.execute_script("window.scrollTo(0, 200)")
time.sleep(3)
browser.find_element(*YANDEX).click()
browser.quit()