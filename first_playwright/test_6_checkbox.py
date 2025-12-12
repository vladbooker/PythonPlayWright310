import random


def test_checkbox(driver_demoqa):  # передали наш браузер из conftest в скобках
    driver_demoqa.goto(
        url="checkbox",
        wait_until="domcontentloaded"
    )

    list_data = random.choice(["Angular", "React", "Veu"])

    success_text_loc = "span[class='text-success']"

    driver_demoqa.get_by_role("button", name="Expand all").click()
    driver_demoqa.get_by_text(list_data).click()

    text = driver_demoqa.locator(success_text_loc).text_content()

    assert text == list_data.lower()

    print(text)
