# -*- coding: utf8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import pytest
import time


GROUP = ("xpath", "(//button[@type='button'])[1]")
ALL_PRODUCT = ("xpath", "//div[contains(@class, 'new-rubricator-content-rootCategory-Du_gW')]")
NAME_PRODUCT = ("xpath", "//strong[@class='styles-module-root-LEIrw styles-module-size_xxl-PtAD9']")


@pytest.fixture
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--ignore-certificate-errors-spki-list")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    browser.get("https://www.avito.ru/")
    yield browser
    browser.quit()


class TestMainPage:

    @pytest.mark.smoke
    def test_function(self, browser):
        wait = WebDriverWait(browser, 5)
        action = ActionChains(browser)
        wait.until(EC.element_to_be_clickable(GROUP)).click()
        all_categories = ['Транспорт', 'Недвижимость', 'Работа', 'Услуги', 'Личные вещи', 'Для дома и дачи', 'Запчасти и аксессуары', 'Электроника', 'Хобби и отдых', 'Животные', 'Бизнес и оборудование', 'Молл']
        search = []

        elements = wait.until(EC.visibility_of_all_elements_located(ALL_PRODUCT))

        for element in elements:
            action.move_to_element(element).perform()
            time.sleep(1)

            name_products = browser.find_element(*NAME_PRODUCT).get_attribute('data-name')
            search.append(name_products)

        assert all_categories == search, f"названия не совпадают, вот что получилось {search}"
        # print(search)


