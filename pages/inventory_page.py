from .base_page import BasePage

class InventoryPage(BasePage):
    # Локаторы
    TITLE = ("css", ".title")
    MENU_BUTTON = ("id", "react-burger-menu-btn")
    LOGOUT_LINK = ("id", "logout_sidebar_link")
    
    def get_title(self):
        return self.find_element(self.TITLE).text
    
    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)