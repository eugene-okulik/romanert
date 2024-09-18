from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('maximize')
    chrome_driver = webdriver.Chrome(options)
    chrome_driver.implicitly_wait(5)
    return chrome_driver


def test_part_three_one(driver):
    language = 'Python'

    driver.get('https://www.qa-practice.com/elements/select/single_select')

    language_dropdown = driver.find_element(By.CLASS_NAME, 'form-select')
    select_language = Select(language_dropdown)
    select_language.select_by_visible_text(language)

    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.result-text')))
    result = driver.find_element(By.CSS_SELECTOR, '.result-text')
    assert result.text == language


def test_part_three_two(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.XPATH, '//*[@id="start"]/button')
    start_button.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'finish')))
    result_text = driver.find_element(By.ID, 'finish')
    assert result_text.text == "Hello World!"
