
def test_download(driver_demoqa):
    driver_demoqa.goto(
        url="upload-download",
        wait_until="domcontentloaded"
    )

    download_btn_loc = "a[id='downloadButton']"
    download_file_path = "/home/sentinel/PycharmProjects/PythonPlaywright310/download"

    with driver_demoqa.expect_download() as download_info:
        driver_demoqa.locator(download_btn_loc).click()

    download = download_info.value

    file_name = download.suggested_filename
    url = download.url
    file_path = download.path()
    page = download.page

    print(file_name)
    print(file_path)
    print(url)
    print(page)

    download.save_as(f"{download_file_path}/{file_name}")


def test_upload(driver_demoqa):
    driver_demoqa.goto(
        url="upload-download",
        wait_until="domcontentloaded"
    )

    upload_file_loc = "input[id='uploadFile']"

    text_info = "p[id='uploadedFilePath']"
    file_path = "/home/sentinel/PycharmProjects/PythonPlaywright310/download/sampleFile.jpeg"

    driver_demoqa.set_input_files(upload_file_loc, file_path)

    text = driver_demoqa.locator(text_info).text_content()

    assert "sampleFile.jpeg" in text
