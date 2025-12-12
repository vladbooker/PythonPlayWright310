# import re
# from playwright.sync_api import Playwright, sync_playwright, expect
#
#
# def run(playwright: Playwright) -> None:
#     # Запускаем браузер (headless=False чтобы видеть процесс)
#     browser = playwright.chromium.launch(headless=False)
#
#     # Создаем контекст
#     context = browser.new_context()
#
#     # Создаем страницу
#     page = context.new_page()
#
#     # Переходим на сайт
#     page.goto("https://www.saucedemo.com/")
#
#     # Проверяем что загрузилось
#     print(f"Сайт загружен: {page.title()}")
#     print(f"URL: {page.url}")
#
#     # Заполняем форму (исправленные локаторы)
#     page.locator("#user-name").fill("standard_user")
#     page.locator("#password").fill("secret_sauce")
#
#     # Ждем немного чтобы увидеть
#     page.wait_for_timeout(1000)
#
#     # Кликаем кнопку входа
#     page.locator("#login-button").click()
#
#     # Ждем перехода
#     page.wait_for_url("**/inventory.html")
#
#     # Проверяем успешный вход
#     print(f"Успешный вход!")
#     print(f"Новый URL: {page.url}")
#
#     # Можно проверить элементы на странице
#     products = page.locator(".inventory_item").count()
#     print(f"Найдено товаров: {products}")
#
#     # Делаем скриншот
#     page.screenshot(path="/tmp/saucedemo_success.png")
#     print("Скриншот сохранен: /tmp/saucedemo_success.png")
#
#     # Ждем перед закрытием (для демонстрации)
#     input("Нажмите Enter чтобы закрыть браузер...")
#
#     # Закрываем
#     context.close()
#     browser.close()
#
#
# if __name__ == "__main__":
#     with sync_playwright() as playwright:
#         run(playwright)
#     print("Тест завершен успешно!")

#----------------------------------------------------------------------------------------------------------------

import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    time.sleep(1)
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    time.sleep(1)
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    time.sleep(1)
    page.locator("[data-test=\"login-button\"]").click()
    time.sleep(3)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)