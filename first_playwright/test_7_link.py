import time


def test_link_click_status_code(driver_demoqa):  # передали наш браузер из conftest в скобках
    driver_demoqa.goto(
        url="links",
        wait_until="domcontentloaded"
    )

    created_link_loc = "a[id='created']"

    with driver_demoqa.expect_response(lambda response: response.status) as response_info:
        driver_demoqa.click(created_link_loc)

    response = response_info.value
    status_code = response.status
    assert status_code == 201, "Status code is not 201"


def test_link_new_tab(driver_demoqa):
    driver_demoqa.goto(
        "links",
        wait_until="domcontentloaded"
    )

    before_url = driver_demoqa.url

    simple_link_loc = "a[id='simpleLink']"

    with driver_demoqa.context.expect_page() as new_page_info:
       driver_demoqa.click(simple_link_loc)

    new_page = new_page_info.value
    after_url = new_page.url

    assert before_url != after_url and after_url == "https://demoqa.com/"


def test_link_new_tab2(driver_demoqa):

    simple_link_loc = "a[id='simpleLink']"

    driver_demoqa.click(simple_link_loc)

    driver_demoqa.wait_for_load_state("domcontentloaded")

    all_pages = driver_demoqa.context.pages

    time.sleep(2)

    original_page = all_pages[0]
    new_page = all_pages[1]
    new_page.bring_to_front()

    print(new_page.url)

    original_page.bring_to_front()
    print(original_page)