from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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


def test_part_two(driver):
    input_data = {
        'first_name_value': 'George',
        'last_name_value': 'Clooney',
        'email_value': 'gclooney1000@gmail.com',
        'phone_value': '3103562398',
        'month_value': '2',
        'year_value': '1990',
        'subject_value': 'Computer science',
        'address_value': 'My current address'
    }

    driver.get('https://demoqa.com/automation-practice-form')

    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys(input_data['first_name_value'])

    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys(input_data['last_name_value'])

    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys(input_data['email_value'])

    gender = driver.find_element(By.CSS_SELECTOR, '[for="gender-radio-1"]')
    gender.click()

    phone_number = driver.find_element(By.CSS_SELECTOR, '#userNumber.mr-sm-2.form-control')
    phone_number.send_keys(input_data['phone_value'])

    birth_date = driver.find_element(By.ID, 'dateOfBirthInput')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'dateOfBirthInput')))
    birth_date.click()

    month_dropdown = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    select_month = Select(month_dropdown)
    select_month.select_by_value(input_data['month_value'])

    year_dropdown = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
    select_year = Select(year_dropdown)
    select_year.select_by_value(input_data['year_value'])

    day_dropdown = driver.find_element(By.CLASS_NAME, 'react-datepicker__day--009')
    day_dropdown.click()

    subjects = driver.find_element(By.ID, 'subjectsInput')
    subjects.send_keys(input_data['subject_value'])
    subjects.send_keys(Keys.ENTER)

    hobbies = driver.find_element(By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[2]/label')
    hobbies.click()

    state = driver.find_element(By.ID, 'state')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'state')))
    state.click()
    state_option = driver.find_element(By.XPATH, '//div[text()="NCR"]')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="NCR"]')))
    state_option.click()

    city = driver.find_element(By.ID, 'city')
    city.click()
    city_option = driver.find_element(By.XPATH, '//div[text()="Delhi"]')
    city_option.click()

    address = driver.find_element(By.ID, 'currentAddress')
    address.send_keys(input_data['address_value'])

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))

    table = driver.find_elements(By.CSS_SELECTOR, '.modal-content .table')

    for row in table:
        print(row.text)
