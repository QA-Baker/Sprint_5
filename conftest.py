import pytest
from selenium import webdriver

BASE_URL = "https://stellarburgers.nomoreparties.site/"


@pytest.fixture
def setup_main_page():
    # Инициализация WebDriver для Chrome и открытие главной страницы
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def setup_register_page():
    # Инициализация WebDriver для Chrome и открытие страницы регистрации
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL + "register")
    yield driver
    driver.quit()


@pytest.fixture
def setup_login_page():
    # Инициализация WebDriver для Chrome и открытие страницы авторизации
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL + "login")
    yield driver
    driver.quit()
