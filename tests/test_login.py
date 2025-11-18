from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    assert inventory_page.get_title() == "PRODUCTS"

def test_logout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.logout()
    
    assert "saucedemo.com" in driver.current_url