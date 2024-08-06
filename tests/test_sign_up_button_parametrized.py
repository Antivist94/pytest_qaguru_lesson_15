import pytest
from selene import browser, be

web_only = pytest.mark.parametrize("browser_manager_web", [(1920, 1080), (1280, 720), (1013, 720)],
                                   ids = ["WEB_width 1920", "WEB_width 1280", "WEB_width 1013"], indirect = True)

mobile_only = pytest.mark.parametrize("browser_manager_mobile", [(320, 640), (360, 740), (412, 869)],
                                      ids = ["Mobile_640x320", "Mobile_740x360", "Mobile_869x412"], indirect = True)


@web_only
def test_sign_up_button_desktop(browser_manager_web):
    browser.open('')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email-container').should(be.visible)


@mobile_only
def test_sign_up_button_mobile(browser_manager_mobile):
    browser.open('')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email-container').should(be.visible)
