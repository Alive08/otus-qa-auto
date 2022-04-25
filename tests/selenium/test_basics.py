


def test_check_title(driver):
    driver.get("http://127.0.0.1:8081/")
    assert "Your Store" == driver.title
    