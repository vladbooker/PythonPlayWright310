import time

def test_simple_drag_and_drop(driver_demoqa):

    driver_demoqa.goto("droppable", wait_until="domcontentloaded")

    drag_loc = "div[id='draggable']"
    drop_loc = "div[id='simpleDropContainer'] div[id='droppable']"

    driver_demoqa.drag_and_drop(drag_loc, drop_loc)

    container_text = driver_demoqa.locator(drop_loc)
    text = container_text.locator("p").inner_text()
    assert text == "Dropped!"