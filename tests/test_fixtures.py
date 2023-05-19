"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser


@pytest.fixture
def test_github_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture
def test_github_mobile():
    browser.config.window_width = 360
    browser.config.window_height = 640


def test_open_github_desktop(test_github_desktop):
    browser.open('https://github.com/')
    browser.config.hold_driver_at_exit = True
    browser.element('a[href="/login"]').click()


def test_open_github_mobile(test_github_mobile):
    browser.open('https://github.com/')
    browser.config.hold_driver_at_exit = True
    browser.element('.Button-content').click()
    browser.element('a[href="/login"]').click()
