from test_UI_playwright_romanert.pages.locators import customer_account_create_locators as loc
from test_UI_playwright_romanert.pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CustomerAccountCreate(BasePage):
    page_url = '/customer/account/create/'

    def __init__(self, page: Page):
        super().__init__(page)

    def click_create_an_account_button(self):
        self.find(loc.create_an_account_button_loc).click()

    def input_password(self, password):
        self.find(loc.password_field).press_sequentially(password, delay=20)

    def clear_password_field(self):
        self.find(loc.password_field).clear()

    def input_password_and_confirm_password(self, password, confirm_password):
        self.find(loc.password_field).press_sequentially(password, delay=20)
        self.find(loc.confirm_password_field).press_sequentially(confirm_password, delay=20)

    def verify_password_strength_meter_text(self, password_meter_text):
        expect(self.find(loc.password_strength_meter)).to_have_text(password_meter_text)

    def verify_password_error_text(self, password_error_text):
        expect(self.find(loc.confirm_password_error_loc)).to_have_text(password_error_text)

    def verify_first_name_required_error_is_displayed(self):
        expect(self.find(loc.first_name_req_error_loc)).to_be_visible()

    def verify_last_name_required_error_is_displayed(self):
        expect(self.find(loc.last_name_req_error_loc)).to_be_visible()

    def verify_email_required_error_is_displayed(self):
        expect(self.find(loc.email_address_req_error_loc)).to_be_visible()

    def verify_password_required_error_is_displayed(self):
        expect(self.find(loc.password_req_error_loc)).to_be_visible()

    def verify_confirm_password_required_error_is_displayed(self):
        expect(self.find(loc.confirm_password_error_loc)).to_be_visible()
