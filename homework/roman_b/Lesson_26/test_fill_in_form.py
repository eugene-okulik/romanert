from playwright.sync_api import Page


def test_fill_in_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')

    input_data = {
        'first_name_value': 'George',
        'last_name_value': 'Clooney',
        'email_value': 'gclooney1000@gmail.com',
        'phone_value': '3103562398',
        'subject_value': 'Computer science',
        'address_value': 'My current address'
    }

    page.get_by_placeholder('First Name').fill(input_data['first_name_value'])
    page.get_by_placeholder('Last Name').fill(input_data['last_name_value'])
    page.get_by_placeholder('name@example.com').fill(input_data['email_value'])
    page.locator('label[for="gender-radio-1"]').click()
    page.get_by_placeholder('Mobile Number').fill(input_data['phone_value'])

    subjects = page.locator('#subjectsInput')
    subjects.fill(input_data['subject_value'])
    subjects.press('Enter')

    page.locator('label[for="hobbies-checkbox-1"]').click()
    page.get_by_placeholder('Current Address').fill(input_data['address_value'])

    page.locator('#state').click()
    page.locator('//*[text()="NCR"]').click()
    page.locator('#city').click()
    page.locator('//*[text()="Delhi"]').click()
    page.get_by_role('button', name="Submit").click()
