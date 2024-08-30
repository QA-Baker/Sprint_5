import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import RegistrationPageLocators, NavigationPageLocators, AuthorizationPageLocators
from utils import generate_email, generate_password


@pytest.mark.usefixtures("setup_register_page")
class TestAuthorization:

    def test_authorization_by_log_in_to_account_button_on_the_main_page(self, setup_register_page):
        driver = setup_register_page

        # Регистрация
        email = generate_email()
        password = generate_password()

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("TestUser")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        # Вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*NavigationPageLocators.LOGO).click()
        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/'))
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT_AU).send_keys(email)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT_AU).send_keys(password)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_AU).click()
        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.find_element(*AuthorizationPageLocators.ADD_ORDER).text == 'Оформить заказ'

    def test_authorization_by_personal_account_button(self, setup_register_page):
        driver = setup_register_page

        # Регистрация
        email = generate_email()
        password = generate_password()

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("TestUser")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        # Вход через кнопку «Личный кабинет»
        driver.find_element(*NavigationPageLocators.LOGO).click()
        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/'))
        driver.find_element(*NavigationPageLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT_AU).send_keys(email)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT_AU).send_keys(password)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_AU).click()
        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.find_element(*AuthorizationPageLocators.ADD_ORDER).text == 'Оформить заказ'

    def test_authorization_by_button_in_the_registration_form(self, setup_register_page):
        driver = setup_register_page

        # Регистрация
        email = generate_email()
        password = generate_password()

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("TestUser")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        # Вход через кнопку в форме регистрации
        driver.find_element(*RegistrationPageLocators.TO_REGISTRATION).click()
        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/register'))
        driver.find_element(*AuthorizationPageLocators.REGISTER_FORM_BUTTON).click()
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT_AU).send_keys(email)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT_AU).send_keys(password)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_AU).click()
        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.find_element(*AuthorizationPageLocators.ADD_ORDER).text == 'Оформить заказ'

    def test_authorization_by_button_in_the_password_recovery_form(self, setup_register_page):
        driver = setup_register_page

        # Регистрация
        email = generate_email()
        password = generate_password()

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("TestUser")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        # Вход через кнопку в форме восстановления пароля
        driver.find_element(*RegistrationPageLocators.TO_PASSWORD_RECOVERY).click()
        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/forgot-password'))
        driver.find_element(*AuthorizationPageLocators.RECOVERY_FORM_BUTTON).click()
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT_AU).send_keys(email)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT_AU).send_keys(password)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_AU).click()
        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.find_element(*AuthorizationPageLocators.ADD_ORDER).text == 'Оформить заказ'

    def test_successful_logout_from_personal_account(self, setup_register_page):
        driver = setup_register_page

        # Регистрация и авторизация
        email = generate_email()
        password = generate_password()

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("TestUser")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT_AU).send_keys(email)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT_AU).send_keys(password)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_AU).click()
        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.find_element(*AuthorizationPageLocators.ADD_ORDER).text == 'Оформить заказ'

        # Выход из аккаунта
        driver.find_element(*NavigationPageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(
            (By.XPATH, "//main/div/nav/ul/li[3]/button[text()='Выход']")))
        driver.find_element(*AuthorizationPageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        assert driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_AU).text == 'Войти'
