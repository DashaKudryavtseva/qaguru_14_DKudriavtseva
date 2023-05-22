"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import browser, have


def test_open_github_desktop(test_github_desktop):
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_open_github_mobile(test_github_mobile):
    browser.element('.Button-content').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
