import pytest
from selenium import webdriver
from config import URLS
from locators import RegistrationPageLocators
from utils import generate_email, generate_password
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope="function")
def create_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(create_driver):
    create_driver.get(URLS["main"])  # Основная страница
    return create_driver


@pytest.fixture
def register_page(create_driver):
    create_driver.get(URLS["register"])  # Страница регистрации
    return create_driver


@pytest.fixture
def login_page(create_driver):
    create_driver.get(URLS["login"])  # Страница логина
    return create_driver


@pytest.fixture
def register_user(create_driver):
    driver = create_driver
    email = generate_email()
    password = generate_password()

    driver.get(URLS["register"])
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("TestUser")
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 3).until(ec.url_to_be(URLS["login"]))

    return email, password, driver
