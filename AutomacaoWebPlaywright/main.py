from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    driver = p.chromium.launch(headless=False)
    page = driver.new_page()
    page.goto("https://www.hashtagtreinamentos.com/curso-python")
    page.locator('xpath=/html/body/div/div[2]/div/div[2]/form/div[1]/input').type("Teste")
    page.locator('xpath=/html/body/div/div[2]/div/div[2]/form/div[2]/input').type("teste@gmail.com")
    page.locator('xpath=/html/body/div/div[2]/div/div[2]/form/button').click()
    time.sleep(5)