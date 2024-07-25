# -*- coding: utf8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


ALL_PRODUCT = ("xpath", "//li[@class='UiKitDesktopShopMenuItem_root']")
NAME_PRODUCT = ("xpath", "//h1[@data-testid='desktop-shop-catalog-page-title']")


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    link = "https://eda.yandex.ru/retail/magnit_celevaya?placeSlug=magnit_celevaya_cp4n8"
    browser.get(link)
    yield browser
    browser.quit()


class TestMainPage():

    @pytest.mark.smoke
    def test_function(self, browser):

        name_magnit_element = ['Скидки и акции', 'Наши бренды', 'Готовая еда', 'Молоко и яйца', 'Овощи и зелень', 'Фрукты и ягоды', 'Сладости', 'Мясо и птица', 'Рыба и морепродукты', 'Заморозка', 'Вода и напитки', 'Колбасы и сосиски', 'Хлеб и выпечка', 'Сыры', 'Макароны и крупы', 'Кофе и чай', 'Все для выпечки и десертов', 'Масло, соусы и специи', 'Консервы и соления', 'Орехи, снеки и чипсы', 'Для детей', 'Красота и гигиена', 'Стирка и уборка', 'Для животных', 'Дом, дача и авто']
        check_name = []
        wait = WebDriverWait(browser, 5)
        self.elements = wait.until(EC.visibility_of_all_elements_located(ALL_PRODUCT))

        for element in range(25):
            self.element_by_magnit = wait.until(EC.visibility_of_all_elements_located(ALL_PRODUCT))
            self.element_by_magnit[element].click()

            self.name_product = wait.until(EC.visibility_of_element_located(NAME_PRODUCT)).text
            check_name.append(self.name_product)
            time.sleep(1)
            browser.back()

        assert name_magnit_element == check_name, f"названия не совпадают, вот что получилось {check_name}"
        print(check_name)

