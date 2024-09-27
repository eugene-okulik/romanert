from test_UI_playwright_romanert.pages.locators import collections_eco_friendly_locators as loc
from test_UI_playwright_romanert.pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CollectionsEcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def __init__(self, page: Page):
        super().__init__(page)
        self.first_item = self.find(loc.first_item_loc)

    def add_item_to_compare(self):
        self.first_item.scroll_into_view_if_needed()
        self.page.evaluate("window.scrollBy(0, 250)")
        self.first_item.hover()
        compare_button = self.find(loc.compare_button_loc).nth(0)
        compare_button.click()

    def verify_item_successfully_added_to_compare(self):
        first_item_name = self.first_item.inner_text()
        you_added_item_banner = self.page.locator(loc.you_added_item_banner_loc)
        expect(you_added_item_banner).to_be_visible()
        expect(you_added_item_banner).to_have_text(f"You added product {first_item_name} to the comparison list.")

    def verify_product_images_load(self):
        first_product_image = self.find(loc.first_product_image_loc)
        fifth_product_image = self.find(loc.fifth_product_image_loc)
        expect(first_product_image).to_be_visible()
        expect(fifth_product_image).to_be_visible()

    def click_erin_recommends_menu_option(self):
        self.find(loc.erin_recommends_loc).click()

    def verify_erin_recommends_submenu_options_clickable(self):
        erin_recommends_yes = self.find(loc.erin_recommends_yes_loc)
        erin_recommends_no = self.find(loc.erin_recommends_no_loc)
        expect(erin_recommends_yes).to_be_enabled()
        expect(erin_recommends_no).to_be_enabled()
