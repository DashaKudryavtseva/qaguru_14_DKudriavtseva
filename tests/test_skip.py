"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import have, browser





@pytest.mark.parametrize("browser_type_for_skip", [
    pytest.param("desktop-1920", marks=[pytest.mark.skip(reason="This parametrize for desktop")]),
    pytest.param("desktop-1280", marks=[pytest.mark.skip(reason="This parametrize for desktop")]),
    pytest.param("desktop-2560", marks=[pytest.mark.skip(reason="This parametrize for desktop")]),
    pytest.param("mobile-360"),
    pytest.param("mobile-480")
], indirect=True)
def test_github_mobile(browser_type_for_skip):
    browser.element('.Button-content').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))



@pytest.mark.parametrize("browser_type_for_skip", [
    pytest.param("desktop-1920"),
    pytest.param("desktop-1280"),
    pytest.param("desktop-2560"),
    pytest.param("mobile-360", marks=[pytest.mark.skip(reason="This parametrize for mobile")]),
    pytest.param("mobile-480", marks=[pytest.mark.skip(reason="This parametrize for mobile")])
], indirect=True)
def test_github_desktop(browser_type_for_skip):
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
