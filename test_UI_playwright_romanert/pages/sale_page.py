from test_UI_playwright_romanert.pages.locators import sale_page_locators as loc
from test_UI_playwright_romanert.pages.base_page import BasePage
from playwright.sync_api import expect


class SalePage(BasePage):
    page_url = '/sale.html'

    def verify_women_deals_categories_clickable(self):
        hoodies_and_sweatshirts = self.find(loc.women_hoodies_and_sweatshirts_loc)
        jackets = self.find(loc.women_jackets_loc)
        tees = self.find(loc.women_tees_loc)
        bras_tanks = self.find(loc.women_bras_tanks_loc)
        pants = self.find(loc.women_bras_tanks_loc)
        shorts = self.find(loc.women_shorts_loc)

        expect(hoodies_and_sweatshirts).to_be_visible()
        expect(jackets).to_be_visible()
        expect(tees).to_be_visible()
        expect(bras_tanks).to_be_visible()
        expect(pants).to_be_visible()
        expect(shorts).to_be_visible()

        expect(hoodies_and_sweatshirts).to_be_enabled()
        expect(jackets).to_be_enabled()
        expect(tees).to_be_enabled()
        expect(bras_tanks).to_be_enabled()
        expect(pants).to_be_enabled()
        expect(shorts).to_be_enabled()

    def verify_men_deals_categories_clickable(self):
        hoodies_and_sweatshirts = self.find(loc.men_hoodies_and_sweatshirts_loc)
        jackets = self.find(loc.men_jackets_loc)
        tees = self.find(loc.men_tees_loc)
        pants = self.find(loc.men_pants_loc)
        shorts = self.find(loc.men_shorts_loc)

        expect(hoodies_and_sweatshirts).to_be_visible()
        expect(jackets).to_be_visible()
        expect(tees).to_be_visible()
        expect(pants).to_be_visible()
        expect(shorts).to_be_visible()

        expect(hoodies_and_sweatshirts).to_be_enabled()
        expect(jackets).to_be_enabled()
        expect(tees).to_be_enabled()
        expect(pants).to_be_enabled()
        expect(shorts).to_be_enabled()

    def verify_banner_images_load(self):
        shop_women_deals = self.find(loc.shop_women_deals_loc)
        shop_men_deals = self.find(loc.shop_men_deals_loc)
        shop_luma_gear = self.find(loc.shop_luma_gear_loc)

        expect(shop_women_deals).to_be_visible()
        expect(shop_men_deals).to_be_visible()
        expect(shop_luma_gear).to_be_visible()
