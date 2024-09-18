from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('maximize')
    chrome_driver = webdriver.Chrome(options)
    return chrome_driver


def test_part_one(driver):
    input_data = 'Levioso'

    driver.get('https://www.qa-practice.com/elements/input/simple')

    input_field = driver.find_element(By.ID, 'id_text_string')
    input_field.send_keys(input_data)
    input_field.submit()
    input_result = driver.find_element(By.ID, 'result-text')

    assert input_result.text == input_data
