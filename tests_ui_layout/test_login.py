import time

from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
# from tests_ui_layout import conftest
# npx playwright codegen demo.playwright.dev/todomvc
# npx playwright codegen https://symonstorozhenko.wixsite.com/website-1
# npx playwright codegen

@pytest.mark.smoke
def test_login(set_up) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")

    # login_issue = True
    # while login_issue:
    #     if not page.is_visible("signUp.switchToSignUp"):
    #         page.get_by_role("button", name="Log In").first.click()
    #     else:
    #         login_issue = False
    #     time.sleep(0.1)

    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Enter")

    # assert page.is_visible("Password")
    page.wait_for_load_state()
    page.wait_for_selector("text=Password")
    expect(page.get_by_text("Password").first).to_be_visible()


    page.get_by_label("Password").fill("test123", timeout=2000)
    page.get_by_label("Password").press("Enter")
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()

    all_links = page.get_by_role("link").all()
    for link in all_links:
        if '$85' in link.text_content():
            assert 'socks' not in link.text_content().lower() and 'notepad' not in link.text_content().lower()
    # product = page.get_by_text('$85').first.locator('xpath=../../../..//h3').text_content()
    # assert product != 'Socks'

    print("Yay!")

    # List of assertions
    # https://playwright.dev/python/docs/test-assertions


with sync_playwright() as playwright:
    test_login(playwright)


# @pytest.mark.skip(reason="not ready")
@pytest.mark.xfail(reason="url not ready")
def test_login_2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")

    # login_issue = True
    # while login_issue:
    #     if not page.is_visible("signUp.switchToSignUp"):
    #         page.get_by_role("button", name="Log In").first.click()
    #     else:
    #         login_issue = False

    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Enter")

    # assert page.is_visible("Password")
    page.wait_for_load_state()
    page.wait_for_selector("text=Password")
    expect(page.get_by_text("Password").first).to_be_visible()


    page.get_by_label("Password").fill("test123", timeout=2000)
    page.get_by_label("Password").press("Enter")
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()

    all_links = page.get_by_role("link").all()
    for link in all_links:
        if '$85' in link.text_content():
            assert 'socks' not in link.text_content().lower() and 'notepad' not in link.text_content().lower()
    # product = page.get_by_text('$85').first.locator('xpath=../../../..//h3').text_content()
    # assert product != 'Socks'

    print("Yay!")

    # List of assertions
    # https://playwright.dev/python/docs/test-assertions

    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_login(playwright)