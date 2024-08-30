from selenium.webdriver.common.by import By


class AuthenticationPageLocators:
    # Поле для ввода имени
    NAME_INPUT = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input")

    # Поле для ввода email
    EMAIL_INPUT = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input")

    # Поле для ввода пароля
    PASSWORD_INPUT = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input")

    # Кнопка для регистрации
    REGISTER_BUTTON = (By.XPATH, "/html/body/div/div/main/div/form/button")

    # Кнопка для входа по кнопке «Войти в аккаунт» на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, "/html/body/div/div/main/section[2]/div/button")

    # Кнопка для входа через «Личный кабинет»
    LOGIN_BUTTON_ACCOUNT = (By.XPATH, "/html/body/div/div/main/div/form/button")

    # Кнопка для входа в форме регистрации
    REGISTER_FORM_BUTTON = (By.XPATH, "/html/body/div/div/main/div/div/p/a")

    # Кнопка для входа в форме восстановления пароля
    RECOVERY_FORM_BUTTON = (By.XPATH, "/html/body/div/div/main/div/div/p/a")

    # Кнопка для выхода из аккаунта
    LOGOUT_BUTTON = (By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button")


class NavigationPageLocators:
    # Кнопка для перехода в личный кабинет
    ACCOUNT_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/a/p")

    # Кнопка для перехода в конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p")

    # Кнопка для перехода в ленту заказов
    ORDER_FEED_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/ul/li[2]/a/p")

    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "/html/body/div/div/header/nav/div")


class ConstructorPageLocators:
    # Кнопка для перехода в раздел «Булки»
    BUNS_SECTION = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[1]/span")

    # Кнопка для перехода в раздел «Соусы»
    SAUCES_SECTION = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]/span")

    # Кнопка для перехода в раздел «Начинки»
    FILLINGS_SECTION = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]/span")
