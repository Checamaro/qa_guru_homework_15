from pages.main_page import main_page
import pytest

@pytest.mark.parametrize('driver', ['desktop'], indirect=True)
def test_desktop(driver):
    main_page.open()
    main_page.click_on_sign_in_desktop()
    main_page.assert_text_sign_in()

@pytest.mark.parametrize('driver', ['mobile'], indirect=True)
def test_mobile(driver):
    main_page.open()
    main_page.click_on_sign_in_mobile()
    main_page.assert_text_sign_in()