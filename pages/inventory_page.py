from .base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    # Локаторы
    TITLE = ("css selector", "[data-test='title']")
    MENU_BUTTON = ("id", "react-burger-menu-btn")
    LOGOUT_LINK = ("id", "logout_sidebar_link")
    
    def get_title(self):
        return self.find_element(self.TITLE).text
    
    def logout(self):
        self.click(self.MENU_BUTTON)
        # Ждем пока меню станет видимым
        self.wait.until(EC.visibility_of_element_located(
            (By.ID, "logout_sidebar_link")
        ))
        self.click(self.LOGOUT_LINK)