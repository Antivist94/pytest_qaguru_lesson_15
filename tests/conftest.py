import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope = "function", params = [(1920, 1080), (1280, 720), (1013, 720)],
                ids = ["WEB_width 1920", "WEB_width 1280", "WEB_width 1013"])
def browser_manager_web(request):
    window_width, window_height = request.param
    browser.config.base_url = 'https://github.com'
    browser.config.window_height = window_height
    browser.config.window_width = window_width

    options = Options()
    options.page_load_strategy.page_load_strategy = 'eager'

    yield browser

    browser.quit()


@pytest.fixture(scope = "function", params = [(320, 640), (360, 740), (412, 869)],
                ids = ["Mobile_640x320", "Mobile_740x360", "Mobile_869x412"])
def browser_manager_mobile(request):
    window_width, window_height = request.param
    browser.config.base_url = 'https://github.com'
    browser.config.window_height = window_height
    browser.config.window_width = window_width

    options = Options()
    options.page_load_strategy.page_load_strategy = 'eager'

    yield browser

    browser.quit()


@pytest.fixture(scope = "function",
                params = [(1920, 1080), (1280, 720), (1013, 720), (320, 640), (360, 740), (412, 869)],
                ids = ["WEB_width 1920", "WEB_width 1280", "WEB_width 1013", "Mobile_640x320", "Mobile_740x360",
                       "Mobile_869x412"])
def browser_manager(request):
    window_width, window_height = request.param
    browser.config.base_url = 'https://github.com'
    browser.config.window_height = window_height
    browser.config.window_width = window_width
    current_window_window_width = int(window_width)

    options = Options()
    options.page_load_strategy.page_load_strategy = 'eager'

    if current_window_window_width >= 1013:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()
