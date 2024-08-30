import pytest
from selenium import webdriver


@pytest.fixture
def setup_main_page():
    # Инициализация WebDriver для Chrome и открытие главной страницы
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture
def setup_register_page():
    # Инициализация WebDriver для Chrome и открытие страницы регистрации
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    yield driver
    driver.quit()
