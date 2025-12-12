import time

# def test1(driver):
#     driver.goto("https://www.saucedemo.com/")
#     time.sleep(1)
#     driver.locator("[data-test='username']").fill("standard_user")
#     time.sleep(1)
#     driver.locator("[data-test='password']").fill("secret_sauce")
#     time.sleep(1)
#     driver.locator("[data-test='login-button']").click()
#     time.sleep(3)

def test(driver):
    driver.goto("https://www.saucedemo.com/")
    username_loc = "[data-test='username']"
    password_loc = "[data-test='password']"
    button_loc = "[data-test='login-button']"
    text_loc = "//div[@class='app_logo']"

    driver.locator(username_loc).fill("standard_user")
    driver.locator(password_loc).fill("secret_sauce")
    driver.locator(button_loc).click()
    text = driver.locator(text_loc).text_content()
    assert text == "Swag Labs", "Text is not Swag Labs"