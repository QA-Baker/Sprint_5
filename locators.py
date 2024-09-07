from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    # Поле для ввода имени
    NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input[@name='name']")

    # Поле для ввода email
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")

    # Поле для ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    # Кнопка для регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button')]")

    # Сообщение об ошибке при вводе короткого пароля
    INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")


class AuthorizationPageLocators:

    # Поле для ввода email
    EMAIL_INPUT_AU = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")

    # Поле для ввода пароля
    PASSWORD_INPUT_AU = (By.XPATH, "//input[@type='password']")

    # Кнопка Войти на странице авторизации
    LOGIN_BUTTON_AU = (By.XPATH, "//button[text()='Войти']")

    # Кнопка «Войти в аккаунт» на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка Войти при входе через «Личный кабинет»
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Кнопка входа в форме регистрации
    REGISTER_FORM_BUTTON = (By.XPATH, "//a[contains(@href, '/login')]")

    # Кнопка входа в форме восстановления пароля
    RECOVERY_FORM_BUTTON = (By.XPATH, "//a[text()='Войти']")

    # Кнопка выхода из аккаунта
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Кнопка оформления заказа
    ADD_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")

    # Кнопка для перехода в окно регистрации со страницы входа в личный кабинет
    TO_REGISTRATION = (By.XPATH, "//a[text()='Зарегистрироваться']")

    # Кнопка для перехода в окно восстановления пароля со страницы входа в личный кабинет
    TO_PASSWORD_RECOVERY = (By.XPATH, "//a[text()='Восстановить пароль']")


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
    CREATE_BURGER = (By.CSS_SELECTOR, "h1.text.text_type_main-large.mb-5.mt-10")


class ConstructorPageLocators:
    # Раздел «Булки»
    BUNS_SECTION = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Булки']/..")

    # Раздел «Соусы»
    SAUCES_SECTION = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Соусы']/..")

    # Раздел «Начинки»
    FILLINGS_SECTION = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Начинки']/..")
