

def test(driver):
    driver.goto("/dynamic_loading/2")

    button_loc = "div[id='start']>button"
    text_loc = "div[id ='finish']>h4"

    driver.locator(button_loc).click()
    text = driver.locator(text_loc).text_content()
    assert text == "Hello World!", "Text is not 'Hello World'"