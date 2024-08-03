import pytest
from selene import browser, be


def test_sign_up_button_desktop(browser_manager):
    if browser_manager == 'mobile':
        pytest.skip("Тест пропущен, так как расширение мобильное")
    browser.open('')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email-container').should(be.visible)


def test_sign_up_button_mobile(browser_manager):
    if browser_manager == 'desktop':
        pytest.skip("Тест пропущен, так как расширение десктопное")
    browser.open('')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email-container').should(be.visible)
