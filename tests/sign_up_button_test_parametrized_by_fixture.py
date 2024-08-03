from selene import browser, be


def test_sign_up_button_desktop(browser_manager_web):
    browser.open('')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email-container').should(be.visible)


def test_sign_up_button_mobile(browser_manager_mobile):
    browser.open('')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email-container').should(be.visible)
