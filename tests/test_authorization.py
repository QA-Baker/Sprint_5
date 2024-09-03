from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import NavigationPageLocators, AuthorizationPageLocators
from config import URLS


class TestAuthorization:

    def test_authorization_by_log_in_to_account_button_on_the_main_page(self, register_user):
        email, password, driver = register_user

        # Вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*NavigationPageLocators.LOGO).click()
        WebDriverWait(driver, 3).until(ec.url_to_be(URLS["main"]))
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT_AU).send_keys(email)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT_AU).send_keys(password)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_AU).click()
        WebDriverWait(driver, 3).until(ec.url_to_be(URLS["main"]))
        assert driver.find_element(*AuthorizationPageLocators.ADD_ORDER).text == 'Оформить заказ'

    def test_authorization_by_personal_account_button(self, register_user):
        email, password, driver = register_user

        # Вход через кнопку «Личный кабинет»
        driver.find_element(*NavigationPageLocators.LOGO).click()
        WebDriverWait(driver, 3).until(ec.url_to_be(URLS["main"]))
        driver.find_element(*NavigationPageLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT_AU).send_keys(email)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT_AU).send_keys(password)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_AU).click()
        WebDriverWait(driver, 3).until(ec.url_to_be(URLS["main"]))
        assert driver.find_element(*AuthorizationPageLocators.ADD_ORDER).text == 'Оформить заказ'

    def test_authorization_by_button_in_the_registration_form(self, register_user):
        email, password, driver = register_user

        # Вход через кнопку в форме регистрации
        driver.find_element(*AuthorizationPageLocators.TO_REGISTRATION).click()
        WebDriverWait(driver, 3).until(ec.url_to_be(URLS["register"]))
        driver.find_element(*AuthorizationPageLocators.REGISTER_FORM_BUTTON).click()
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT_AU).send_keys(email)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT_AU).send_keys(password)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_AU).click()
        WebDriverWait(driver, 3).until(ec.url_to_be(URLS["main"]))
        assert driver.find_element(*AuthorizationPageLocators.ADD_ORDER).text == 'Оформить заказ'

    def test_authorization_by_button_in_the_password_recovery_form(self, register_user):
        email, password, driver = register_user

        # Вход через кнопку в форме восстановления пароля
        driver.find_element(*AuthorizationPageLocators.TO_PASSWORD_RECOVERY).click()
        WebDriverWait(driver, 3).until(ec.url_to_be(URLS["forgot_password"]))
        driver.find_element(*AuthorizationPageLocators.RECOVERY_FORM_BUTTON).click()
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT_AU).send_keys(email)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT_AU).send_keys(password)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_AU).click()
        WebDriverWait(driver, 3).until(ec.url_to_be(URLS["main"]))
        assert driver.find_element(*AuthorizationPageLocators.ADD_ORDER).text == 'Оформить заказ'

    def test_successful_logout_from_personal_account(self, register_user):
        email, password, driver = register_user

        # Авторизация
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT_AU).send_keys(email)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT_AU).send_keys(password)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_AU).click()
        WebDriverWait(driver, 3).until(ec.url_to_be(URLS["main"]))
        assert driver.find_element(*AuthorizationPageLocators.ADD_ORDER).text == 'Оформить заказ'

        # Выход из аккаунта
        driver.find_element(*NavigationPageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.url_to_be(URLS["account_profile"]))
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(AuthorizationPageLocators.LOGOUT_BUTTON))
        driver.find_element(*AuthorizationPageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.url_to_be(URLS["login"]))
        assert driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON_AU).text == 'Войти'
