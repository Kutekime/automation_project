from .base_page import BasePage

class LoginPage(BasePage):
    # Локаторы
    USERNAME_INPUT = ("id", "user-name")
    PASSWORD_INPUT = ("id", "password") 
    LOGIN_BUTTON = ("id", "login-button")
    
    def open(self):
        self.driver.get("https://www.saucedemo.com")
    
    def login(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)