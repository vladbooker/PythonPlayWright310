

def test_tc_01_001_01(page):
    page.goto("/")

    expected_url = "http://localhost:8080/manage/"
    username = "Vlad"
    password = "sifiny99"

    username_field_loc = "input[id='j_username']"
    password_field_loc = "input[id='j_password']"
    submit_btn_loc = "button[name='Submit']"
    user_settings_btn_loc = "a[id='root-action-ManageJenkinsAction']"

    with page.expect_response(lambda response: response.status) as response_info:  # конструкция для перехвата и проверки сетевых ответов при взаимодействии с веб-страницей
     page.locator(user_settings_btn_loc).click()

    response = response_info.value
    status_code = response.status
    print(status_code)

    actual_url = page.url
    assert actual_url == expected_url