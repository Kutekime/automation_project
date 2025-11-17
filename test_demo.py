from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# def test_open_page():
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
    
#     driver.get("https://demoqa.com")
#     title = driver.title
#     assert "ToolsQA" in title
    
#     driver.quit()

def test_open_page():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://demoqa.com")
    title = driver.title
    expected_title = "DEMOQA"
    
    assert title == expected_title, f"Ожидался заголовок '{expected_title}', но получили '{title}'"
    
    driver.quit()