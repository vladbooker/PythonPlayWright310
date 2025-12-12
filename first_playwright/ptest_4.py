from functions import check_time


# def test(driver_demoqa):
#     driver_demoqa.goto(
#         url="/buttons",
#         wait_until="load"
#     )
#
#     button_loc = "button[id='doubleClickBtn']"
#     text_loc = "p[id='doubleClickMessage']"
#
#     driver_demoqa.locator(button_loc).dblclick()
#     text = driver_demoqa.locator(text_loc).text_content()
#     assert text == "You have done a double click"


def test(driver):
    driver.goto(
        url="/buttons"
    )

    button_loc = "button[id='rightClickBtn']"
    text_loc = "p[id='rightClickMessage']"

    driver.locator(button_loc).click(button="right")
    text = driver.locator(text_loc).text_content()
    assert text == "You have done a right click"