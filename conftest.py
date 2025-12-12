import pytest
from playwright.sync_api import Playwright, sync_playwright, ViewportSize
#https://the-internet.herokuapp.com

@pytest.fixture
def driver_hero():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        viewport=ViewportSize(width=1400, height=800),  # можно поменять размер окна браузера
        base_url="https://the-internet.herokuapp.com"  # храним базовый урл здесь
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()
    playwright.stop()

@pytest.fixture
def driver_demoqa():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(
        viewport=ViewportSize(width=1600, height=1000),  # можно поменять размер окна браузера
        base_url="https://demoqa.com/"  # храним базовый урл здесь
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()
    playwright.stop()