from playwright.sync_api import Page


def test_get_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')

    username = 'my_username'
    password = 'my_password'

    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='Username').fill(username)
    page.get_by_role('textbox', name='Password').fill(password)

    page.get_by_role('button', name='Login').click()
