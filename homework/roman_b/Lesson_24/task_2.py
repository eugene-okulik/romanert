from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('maximize')
    chrome_driver = webdriver.Chrome(options)
    return chrome_driver


def test_two(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    first_item = driver.find_element(By.XPATH, '//*[@class="product-item-link"][1]')
    compare_button = driver.find_element(By.XPATH, '//*[@class="action tocompare"][1]')

    first_item_name = first_item.text
    ActionChains(driver).move_to_element(first_item).click(compare_button).perform()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '#compare-items > li > strong > a')))

    assert driver.find_element(By.CSS_SELECTOR, '#compare-items > li > strong > a').text == first_item_name
