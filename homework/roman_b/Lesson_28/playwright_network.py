from playwright.sync_api import Page, expect, Route
import json
import re


def test_modify_response(page: Page):
    honest_name = 'ApplePhone 13S'

    def modify_name(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]['familyTypes'][0]['productName'] = honest_name
        body = json.dumps(body)
        route.fulfill(
            body=body
        )

    page.route(re.compile('/shop/api/digital-mat'), modify_name)
    page.goto('https://www.apple.com/shop/buy-iphone')

    popup = page.locator('.rf-hcard-secondary-cta.button.button-secondary-alpha').locator('nth=0')
    popup.click()
    title = page.locator('//*[@data-autom="DigitalMat-overlay-header-0-0"]')
    expect(title).to_have_text(honest_name)
