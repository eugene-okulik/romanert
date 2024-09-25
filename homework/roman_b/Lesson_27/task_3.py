from playwright.sync_api import Page, expect


def test_wait_for_element_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_change_button = page.locator('#colorChange')
    page.wait_for_selector('.text-danger')
    color_change_button.click()


def test_wait_for_element_change_2(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_change_button = page.locator('#colorChange')
    visible_after_button = page.locator('#visibleAfter')
    expect(visible_after_button).to_be_visible(timeout=7000)
    color_change_button.click()
