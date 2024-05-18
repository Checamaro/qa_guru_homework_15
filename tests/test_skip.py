import pytest
from selene import browser
from pages.main_page import main_page

def test_github_desktop(driver_setup):
    if browser.config.window_width < 1000:
        pytest.skip('Test for mobile')
    main_page.open()
    main_page.click_on_sign_in_desktop()
    main_page.assert_text_sign_in()


def test_github_mobile(driver_setup):
    if browser.config.window_width >= 1000:
        pytest.skip('Test for desktop')
    main_page.open()
    main_page.click_on_sign_in_mobile()
    main_page.assert_text_sign_in()