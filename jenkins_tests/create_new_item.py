import random
import time

def test_tc_01_001_01(page):
    page.goto("/")
    username = "Vlad"
    password = "sifiny99"
    new_item_name = f"Vlad-{random.randint(0,9999)}"

    username_field_loc = "input[id='j_username']"
    password_field_loc = "input[id='j_password']"
    submit_btn_loc = "button[name='Submit']"

    new_item_btn_loc = "a[href='/view/all/newJob']"
    item_name_field_loc = "input[class='jenkins-input']"
    item_type_text = "Pipeline"
    ok_btn_loc = "button[id='ok-button']"
    logo_loc = "a[class='app-jenkins-logo']"
    created_item_loc = f"td > a[href='job/{new_item_name}/']"

    # page.locator(username_field_loc).fill(username)
    # page.locator(password_field_loc).fill(password)
    # page.locator(submit_btn_loc).click()

    page.locator(new_item_btn_loc).click()  # Клик по кнопке new item
    page.locator(item_name_field_loc).fill(new_item_name)
    page.get_by_text(item_type_text, exact=True).click()
    page.locator(ok_btn_loc).click()
    page.locator(logo_loc).click()  # Клик по лого
    text = page.locator(created_item_loc).text_content()  # Получение текста созданного item

    assert text == new_item_name

def test(delete_jobs):
    assert 1==1