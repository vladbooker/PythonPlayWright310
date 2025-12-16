import random

def test_tc_21_010_002(page):

    page.goto("/")
    random_text = f"Vlad-{random.randint(0, 999999)}-Vlad"

    add_description_btn_loc = "a[id='description-link']"
    description_field_loc = "textarea[name='description']"
    save_btn_loc = "button[formnovalidate='formNoValidate']"
    description_text_loc = "div[id='description-content']"

    page.click(add_description_btn_loc)
    page.locator(description_field_loc).fill(random_text)
    page.locator(save_btn_loc).click()

    text = page.locator(description_text_loc).text_content()
    print(text)

    assert text == random_text