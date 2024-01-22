from playwright.sync_api import Playwright, sync_playwright, expect

# npx playwright codegen demo.playwright.dev/todomvc
# npx playwright codegen

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Enter")
    page.get_by_label("Password").fill("test123", timeout=2000)
    page.get_by_label("Password").press("Enter")
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    print("Yay!")

    # List of assertions
    # https://playwright.dev/python/docs/test-assertions

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
