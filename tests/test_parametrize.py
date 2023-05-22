"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
from selene import browser, have
import pytest


@pytest.mark.parametrize("browser_type", ['desktop'], indirect=True)
def test_github_desktop(browser_type):
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_type", ['mobile'], indirect=True)
def test_github_mobile(browser_type):
    browser.element('.Button-content').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
