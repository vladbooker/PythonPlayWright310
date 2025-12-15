import pytest
import requests
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


@pytest.fixture
def page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        viewport=ViewportSize(width=1440, height=980),
        base_url="http://localhost:8080"
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()

api_token = "11e0fbe05faa66ec576c17ba64859bfa52"
user_name = "Vlad"
url = "http://localhost:8080/"

def get_all_jobs():
    response = requests.get(
        url=f"{url}api/json",
        auth=(user_name, api_token)
    )
    return response.json()['jobs']

def delete_jobs():
    jobs_list = get_all_jobs()

    for job in jobs_list:
        name = job["name"]
        requests.post(
            url= f"{url}/job/{name}/doDelete",
            auth= (user_name, api_token)
        )

@pytest.fixture(scope="session", autouse=True)
def delete_jobs_after_all_tests():
    yield
    delete_jobs()