from selene import browser, have


class MainPage:
    def open(self):
        browser.open('https://github.com')
        return self

    def click_on_sign_in_desktop(self):
        browser.element('.HeaderMenu-link--sign-in').click()

    def click_on_sign_in_mobile(self):
        browser.element('d-inline-block d-lg-none flex-order-1').click()

    def assert_text_sign_in(self):
        browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


main_page = MainPage()
