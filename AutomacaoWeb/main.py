from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get(
    "https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")


def find_element_by_xpath(navegador, xpath):
    count = 0
    while count < 3:
        try:
            is_exists = navegador.find_element('xpath', xpath)
            print(is_exists)
        except:
            print(" deu ruim")
        count += 1



find_element_by_xpath(driver, "aaaaaaaaa")
