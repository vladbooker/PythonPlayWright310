import time

dropdown_loc = "select[id='dropdown']"

def test_dropdown_value1(driver_hero):

    driver_hero.goto("/dropdown")

    driver_hero.select_option(dropdown_loc, value="1")

    assert driver_hero.locator(dropdown_loc).input_value() == "1"


def test_dropdown_value2(driver_hero):

    driver_hero.goto("/dropdown")

    driver_hero.select_option(dropdown_loc, value="2")

    assert driver_hero.locator(dropdown_loc).input_value() == "2"


def test_dropdown_index1(driver_hero):

    driver_hero.goto("/dropdown")

    driver_hero.select_option(dropdown_loc, index=1)

    assert driver_hero.locator(dropdown_loc).input_value() == "1"


def test_dropdown_label(driver_hero):

    driver_hero.goto("/dropdown")

    driver_hero.select_option(dropdown_loc, label="Option 2")

    selected_option = driver_hero.locator(f"{dropdown_loc} option: checked").all_inner_texts()

    assert selected_option == "Option 2"



