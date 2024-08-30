from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    # Поле для ввода имени
    NAME_INPUT = (By.XPATH, ".//fieldset[1]/div/div/input")

    # Поле для ввода email
    EMAIL_INPUT = (By.XPATH, ".//fieldset[2]/div/div/input")

    # Поле для ввода пароля
    PASSWORD_INPUT = (By.XPATH, ".//fieldset[3]/div/div/input")

    # Кнопка для регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button')]")

    # Кнопка для перехода в окно регистрации со страницы входа в личный кабинет
    TO_REGISTRATION = (By.XPATH, "//p[1]/a[text()='Зарегистрироваться']")

    # Кнопка для перехода в окно восстановления пароля
    TO_PASSWORD_RECOVERY = (By.XPATH, "//p[2]/a[text()='Восстановить пароль']")


class AuthorizationPageLocators:

    # Поле для ввода email
    EMAIL_INPUT_AU = (By.XPATH, ".//form/fieldset[1]/div/div/input")

    # Поле для ввода пароля
    PASSWORD_INPUT_AU = (By.XPATH, ".//form/fieldset[2]/div/div/input")

    # Кнопка Войти на странице авторизации
    LOGIN_BUTTON_AU = (By.XPATH, ".//main/div/form/button")

    # Кнопка «Войти в аккаунт» на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка Вход при входе через «Личный кабинет»,
    ENTER_BUTTON = (By.XPATH, "//main/div/form/button")

    # Кнопка входа в форме регистрации
    REGISTER_FORM_BUTTON = (By.XPATH, "//a[contains(@href, '/login')]")

    # Кнопка входа в форме восстановления пароля
    RECOVERY_FORM_BUTTON = (By.XPATH, ".//main/div/div/p/a[text()='Войти']")

    # Кнопка выхода из аккаунта
    LOGOUT_BUTTON = (By.XPATH, "//main/div/nav/ul/li[3]/button[text()='Выход']")

    # Кнопка оформления заказа
    ADD_ORDER = (By.XPATH, "//main/section[2]/div/button")


class NavigationPageLocators:
    # Кнопка перехода в личный кабинет
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Кнопка перехода на страницу конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")

    # Кнопка перехода в ленту заказов
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

    # Логотип Stellar Burgers
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

    # Надпись Соберите бургер на странице Конструктор
    CREATE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")


class ConstructorPageLocators:
    # Кнопка перехода в раздел «Булки»
    BUNS_SECTION = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Булки']")

    # Кнопка перехода в раздел «Соусы»
    SAUCES_SECTION = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Соусы']")

    # Кнопка перехода в раздел «Начинки»
    FILLINGS_SECTION = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Начинки']")

    # Локаторы ингредиентов
    SAUCE = (By.XPATH, "//section[1]/div[2]/ul[2]/a[1]/img")
    FILLING = (By.XPATH, "//section[1]/div[2]/ul[3]/a[1]/img")
    BUN = (By.XPATH, "//section[1]/div[2]/ul[1]/a[1]/img")
