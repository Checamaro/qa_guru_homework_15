from pages.main_page import main_page


def test_desktop(desktop):
    main_page.open()
    main_page.click_on_sign_in_desktop()
    main_page.assert_text_sign_in()


def test_mobile(mobile):
    main_page.open()
    main_page.click_on_sign_in_mobile()
    main_page.assert_text_sign_in()
