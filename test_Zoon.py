 # -*- coding: utf8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


ENTRY = ("xpath", "//span[text()='Вход']")
EMAIL = ("xpath", "//input[@data-uitest='input-email']")
PASSWORD = ("xpath", "//input[@data-uitest='input-pass']")
ENTER = ("xpath", "(//button[@type='submit'])[2]")
PROFILE = ("xpath", "//div[@class='header-avatar-img round bg-cover']")
SPECIALIST = ("xpath", "//div[@class='button button44']")
COACH = ("xpath", "//a[text()='Тренеры']")
ADDRESS = ("xpath", "//a[@href='mailto:corp@zoon.ru']")


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    link = "https://zoon.ru/"
    browser.get(link)
    yield browser
    browser.quit()


class TestAuthorizations:

    # Негативный тест с невалидными данными
    def test_input_date_1(self, browser):
        wait = WebDriverWait(browser, 4)
        wait.until(EC.visibility_of_element_located(ENTRY)).click()
        wait.until(EC.visibility_of_element_located(EMAIL)).send_keys("kolie#$%-1990^mail.ru")
        wait.until(EC.visibility_of_element_located(PASSWORD)).send_keys(19121985)
        wait.until(EC.visibility_of_element_located(ENTER)).click()
        assert wait.until(EC.visibility_of_element_located(PROFILE)).is_enabled(), f"данные не валидны"

    # Негативный тест с невалидными данными
    def test_input_date_2(self, browser):
        wait = WebDriverWait(browser, 4)
        wait.until(EC.visibility_of_element_located(ENTRY)).click()
        wait.until(EC.visibility_of_element_located(EMAIL)).send_keys("КОЛЕСНИК-1990@mail.ru")
        wait.until(EC.visibility_of_element_located(PASSWORD)).send_keys("")
        wait.until(EC.visibility_of_element_located(ENTER)).click()
        assert wait.until(EC.visibility_of_element_located(PROFILE)).is_enabled(), f"данные не валидны"

    # Негативный тест с невалидными данными
    def test_input_date_3(self, browser):
        wait = WebDriverWait(browser, 4)
        wait.until(EC.visibility_of_element_located(ENTRY)).click()
        wait.until(EC.visibility_of_element_located(EMAIL)).send_keys("")
        wait.until(EC.visibility_of_element_located(PASSWORD)).send_keys("")
        wait.until(EC.visibility_of_element_located(ENTER)).click()
        assert wait.until(EC.visibility_of_element_located(PROFILE)).is_enabled(), f"данные не валидны"

    # Валидные данные. Авторизация проходит успешно
    def test_input_date_4(self, browser):
        wait = WebDriverWait(browser, 4)
        wait.until(EC.visibility_of_element_located(ENTRY)).click()
        wait.until(EC.visibility_of_element_located(EMAIL)).send_keys("koliesnik-1990@mail.ru")
        wait.until(EC.visibility_of_element_located(PASSWORD)).send_keys("Q19121985")
        wait.until(EC.visibility_of_element_located(ENTER)).click()
        assert wait.until(EC.visibility_of_element_located(PROFILE)).is_enabled(), f"данные не валидны"


class TestMainPage:

    # Регистрируемся. Прокручиваем страницу вниз до специалистов и выбираем тренеров.
    # Прокручиваем вниз и проверяем почту указанную на странице
    @pytest.mark.smoke
    def test_function(self, browser):

        wait = WebDriverWait(browser, 4)
        wait.until(EC.visibility_of_element_located(ENTRY)).click()
        wait.until(EC.visibility_of_element_located(EMAIL)).send_keys("koliesnik-1990@mail.ru")
        wait.until(EC.visibility_of_element_located(PASSWORD)).send_keys("Q19121985")
        wait.until(EC.visibility_of_element_located(ENTER)).click()
        time.sleep(1)
        browser.execute_script("window.scrollBy(100, 2000)")
        time.sleep(1)
        wait.until(EC.visibility_of_element_located(SPECIALIST)).click()
        wait.until(EC.visibility_of_element_located(COACH)).click()
        browser.execute_script("window.scrollBy(0, 9000)")
        time.sleep(3)
        email_to_page = "corp@zoon.ru"
        email_to_xpath = wait.until(EC.visibility_of_element_located(ADDRESS)).text
        assert email_to_page == email_to_xpath, f"названия не совпадают, вот что получилось {email_to_xpath}"







    # @pytest.mark.parametrize("input_email","input_password",
    #                          [('', 12343567),
    #                           ('Ivanov@yandex.rus', ),
    #                           ('Иванов@mail.ru', 'qwerty'),
    #                           ('Ivanov@yandex.rus', 12343567),
    #                           ('$%79&|@mail.ru', '123*%$@')])
    #
    # def test_func(self, input_email, input_password):
    #     wait = WebDriverWait(driver, 5)
    #     input_email =

