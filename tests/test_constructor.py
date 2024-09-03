from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import (ConstructorPageLocators, AuthorizationPageLocators, NavigationPageLocators)


class TestConstructorNavigate:

    def test_transition_to_your_personal_account_page(self, main_page):
        driver = main_page
        driver.find_element(*NavigationPageLocators.ACCOUNT_BUTTON).click()
        assert WebDriverWait(driver, 2).until(
            ec.visibility_of_element_located(AuthorizationPageLocators.ENTER_BUTTON))

    def test_transition_to_constructor_by_clicking_on_the_constructor(self, login_page):
        driver = login_page
        driver.find_element(*NavigationPageLocators.CONSTRUCTOR_BUTTON).click()
        assert WebDriverWait(driver, 2).until(
            ec.visibility_of_element_located(NavigationPageLocators.CREATE_BURGER))

    def test_transition_to_constructor_by_clicking_on_logo(self, login_page):
        driver = login_page
        driver.find_element(*NavigationPageLocators.LOGO).click()
        assert WebDriverWait(driver, 2).until(
            ec.visibility_of_element_located(NavigationPageLocators.CREATE_BURGER))

    def test_transition_to_buns_section(self, main_page):
        driver = main_page

        buns_section = driver.find_element(*ConstructorPageLocators.BUNS_SECTION)

        # Проверяем, что 'current' присутствует в секции "Булки" по умолчанию
        assert 'current' in buns_section.get_attribute('class')

        # Переход к другой секции, чтобы проверить, что 'current' уходит
        driver.find_element(*ConstructorPageLocators.SAUCES_SECTION).click()
        buns_section = driver.find_element(*ConstructorPageLocators.BUNS_SECTION)
        assert 'current' not in buns_section.get_attribute('class')

        # Клик по секции "Булки" и проверка на наличие 'current'
        buns_section.click()
        buns_section = driver.find_element(*ConstructorPageLocators.BUNS_SECTION)
        assert 'current' in buns_section.get_attribute('class')

    def test_transition_to_sauces_section(self, main_page):
        driver = main_page

        sauces_section = driver.find_element(*ConstructorPageLocators.SAUCES_SECTION)

        # Проверяем, что 'current' отсутствует в секции "Соусы" до клика
        assert 'current' not in sauces_section.get_attribute('class')

        sauces_section.click()
        sauces_section = driver.find_element(*ConstructorPageLocators.SAUCES_SECTION)

        # Проверяем, что после клика в секции "Соусы" присутствует 'current'
        assert 'current' in sauces_section.get_attribute('class')

    def test_transition_to_fillings_section(self, main_page):
        driver = main_page

        fillings_section = driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION)

        # Проверяем, что 'current' отсутствует в секции "Начинки" до клика
        assert 'current' not in fillings_section.get_attribute('class')

        fillings_section.click()
        fillings_section = driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION)

        # Проверяем, что после клика в секции "Начинки" присутствует 'current'
        assert 'current' in fillings_section.get_attribute('class')
