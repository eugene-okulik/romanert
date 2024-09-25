from playwright.sync_api import Page, expect, BrowserContext


def test_multiple_pages(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    click_button = page.locator('#new-page-button')

    with context.expect_page() as new_page_event:
        click_button.click()

    page_2 = new_page_event.value
    result = page_2.locator('#result-text')
    expect(result).to_have_text("I am a new page in a new tab")

    expect(click_button).to_be_enabled()
