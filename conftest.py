import pytest
from selene import browser


@pytest.fixture
def test_github_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com/')

    yield

    browser.quit()


@pytest.fixture
def test_github_mobile():
    browser.config.window_width = 360
    browser.config.window_height = 640
    browser.open('https://github.com/')

    yield

    browser.quit()


@pytest.fixture(params=['desktop', 'mobile'])
def browser_type(request):
    if request.param == 'mobile':
        browser.config.window_width = 360
        browser.config.window_height = 640
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    browser.open('https://github.com/')

    yield

    browser.quit()

@pytest.fixture()
def browser_type_for_skip(request):
    if request.param == 'mobile-360':
        browser.config.window_width = 360
        browser.config.window_height = 640
    elif request.param == 'mobile-480':
        browser.config.window_width = 480
        browser.config.window_height = 800
    elif request.param == 'desktop-1920':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == 'desktop-1280':
        browser.config.window_width = 1280
        browser.config.window_height = 720
    elif request.param == 'desktop-2560':
        browser.config.window_width = 2560
        browser.config.window_height = 1440

    browser.open('https://github.com/')

    yield

    browser.quit()
