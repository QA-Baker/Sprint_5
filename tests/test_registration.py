from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import RegistrationPageLocators, AuthorizationPageLocators
from utils import generate_email
from config import URLS


class TestRegistration:

    def test_successful_registration(self, register_user):
        email, password, driver = register_user

        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT_AU).send_keys(email)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT_AU).send_keys(password)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_AU).click()
        WebDriverWait(driver, 3).until(ec.url_to_be(URLS["main"]))
        assert driver.find_element(*AuthorizationPageLocators.ADD_ORDER).text == 'Оформить заказ'

    def test_registration_with_invalid_password(self, register_page):
        driver = register_page
        email = generate_email()

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("TestUser")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(driver, 3).until(
                ec.visibility_of_element_located(RegistrationPageLocators.INCORRECT_PASSWORD)
            )
        assert error_message.is_displayed()
