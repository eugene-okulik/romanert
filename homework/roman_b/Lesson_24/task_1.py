from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('maximize')
    chrome_driver = webdriver.Chrome(options)
    return chrome_driver


def test_one(driver):
    driver.get('https://www.demoblaze.com/index.html')

    (WebDriverWait(driver, 5).
     until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[href^="prod.html?idp_=1"]'))))

    product_item = driver.find_element(By.XPATH, '//*[@href="prod.html?idp_=1" and @class="hrefch"]')
    product_name = product_item.text
    driver.execute_script("window.open(arguments[0].href, '_blank');", product_item)

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    add_to_cart = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.btn-success')))
    add_to_cart.click()

    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()

    driver.close()
    driver.switch_to.window(tabs[0])

    driver.find_element(By.ID, 'cartur').click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.success')))
    product_name_from_cart = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]').text

    assert product_name_from_cart == product_name
