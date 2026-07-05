from selenium.webdriver.common.by import By

class LoginPage:
    # 1. Selectores (Localizadores)
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    TITLE_PRODUCTS = (By.CLASS_NAME, "title")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    # 2. Inicialización
    def __init__(self, driver):
        self.driver = driver

    # 3. Métodos de acción
    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_title_text(self):
        return self.driver.find_element(*self.TITLE_PRODUCTS).text

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text