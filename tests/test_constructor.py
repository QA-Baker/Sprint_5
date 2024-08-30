from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import (ConstructorPageLocators, AuthorizationPageLocators, NavigationPageLocators)


class TestConstructorNavigate:

    def test_transition_to_your_personal_account_page(self, setup_main_page):
        driver = setup_main_page
        driver.find_element(*NavigationPageLocators.ACCOUNT_BUTTON).click()
        assert WebDriverWait(driver, 2).until(
            ec.visibility_of_element_located(AuthorizationPageLocators.ENTER_BUTTON))

    def test_transition_to_constructor_by_clicking_on_the_constructor(self, setup_login_page):
        driver = setup_login_page
        driver.find_element(*NavigationPageLocators.CONSTRUCTOR_BUTTON).click()
        assert WebDriverWait(driver, 2).until(
            ec.visibility_of_element_located(NavigationPageLocators.CREATE_BURGER))

    def test_transition_to_constructor_by_clicking_on_logo(self, setup_login_page):
        driver = setup_login_page
        driver.find_element(*NavigationPageLocators.LOGO).click()
        assert WebDriverWait(driver, 2).until(
            ec.visibility_of_element_located(NavigationPageLocators.CREATE_BURGER))

    def test_transition_to_sauce_section(self, setup_main_page):
        driver = setup_main_page
        driver.find_element(*ConstructorPageLocators.SAUCES_SECTION).click()
        assert WebDriverWait(driver, 2).until(
            ec.visibility_of_element_located(ConstructorPageLocators.SAUCE))

    def test_transition_to_fillings_section(self, setup_main_page):
        driver = setup_main_page
        driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION).click()
        assert WebDriverWait(driver, 2).until(
            ec.visibility_of_element_located(ConstructorPageLocators.FILLING))

    def test_transition_to_buns_section(self, setup_main_page):
        driver = setup_main_page
        driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION).click()
        driver.find_element(*ConstructorPageLocators.BUNS_SECTION).click()
        assert WebDriverWait(driver, 2).until(
            ec.visibility_of_element_located(ConstructorPageLocators.BUN))
