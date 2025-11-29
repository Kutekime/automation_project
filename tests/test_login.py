import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestLogin:
    @pytest.mark.parametrize("username,password,expected", [
        ("standard_user", "secret_sauce", True),    # валидные данные
        ("locked_out_user", "secret_sauce", False), # заблокированный пользователь  
        ("invalid_user", "invalid_pass", False),    # неверные данные
        ("", "secret_sauce", False),                # пустой логин
        ("standard_user", "", False),               # пустой пароль
    ])
    
    def test_login_with_different_credentials(self, driver, username, password, expected):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        login_page.open()
        login_page.login(username, password)
        
        if expected:
            # Ожидаем успешный логин
            assert "inventory" in driver.current_url
            assert inventory_page.get_title() == "Products"
        else:
            # Ожидаем ошибку логина
            assert "inventory" not in driver.current_url

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    assert inventory_page.get_title() == "Products"

def test_logout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.logout()
    
    assert "saucedemo.com" in driver.current_url