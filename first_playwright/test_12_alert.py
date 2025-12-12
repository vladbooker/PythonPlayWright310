import time


def test_confirm_alert_example(driver_demoqa):

    driver_demoqa.goto("alerts", wait_until="domcontentloaded")

    confirm_btn_loc = "button[id='confirmButton']"

    driver_demoqa.click(confirm_btn_loc)

    time.sleep(2)