# Sporty Tech Test

This project contains UI and API tests using Python's [pytest](https://docs.pytest.org/en/stable/) framework. 

The tests demonstrate these two primary features: 
- Twitch UI with [pytest-selenium](https://pytest-selenium.readthedocs.io/)
- Dog API with the [requests](https://requests.readthedocs.io/en/latest/) library

---

## 📋 Prerequisites

### 🛠 Environment Setup

Ensure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [Homebrew](https://brew.sh/) (for macOS users)
- [pipx](https://pipx.pypa.io/stable/installation/)
- [Poetry](https://python-poetry.org/docs/)

### 🌐 Web Drivers for UI Tests

For the UI tests, you will need the appropriate browser driver:

- [Chrome Webdriver](https://googlechromelabs.github.io/chrome-for-testing/)

---

## 📦 Installing Dependencies

To install the project dependencies, run the following command from the root of the project directory:

```bash
poetry install
```

## 🖥 Twitch UI Tests

The Twitch UI tests use the Google Chrome Emulator to simulate an Android mobile phone.

### ▶ Running UI Tests

To run the UI tests, use the following command:

```bash
poetry run pytest twitch/tests/test_twitch.py
```

Here's a GIF showing the test run:

![Twitch UI Tests](twitch/gif/twitch_recording.gif)

### Available Helper Functions

To support contributions, reusable helper functions are available in the `twitch/tests/conftest.py` file. 

Here’s a summary of those functions:

| Test Name                          | Function                             |
|------------------------------------|--------------------------------------|
| wait_for_element()                 | Wait for presence of element (xpath) |
| click_xpath(driver, xpath)         | Clicks on element with given xpath   |
| emulator()                         | Sets up mobile emulator              |
| rejects_cookies(driver)            | Rejects cookies                      |
| browse(driver)                     | Clicks on browse                     |
| search(driver, search_term)        | Search using a given string          |     
| click_partial_text(driver, option) | Clicks on link using a given string  |
| capture_screenshot(driver)         | Captures screenshot                  |
| scroll(driver)                     | Scrolls down                         |

### ⚠ Known Issue: Scrolling

After following the documentation, the `scroll()` function does not appear to work for Twitch UI tests because the viewport is empty. 

This can be verified by using the `screenshot()` function before calling `scroll()`.

This issue requires further investigation, but the `scroll()` function is still available for use in the meantime.

### 🔮 Future Improvements

- Investigate and resolve the scrolling issue.
- Run tests across multiple devices and screen sizes to ensure broader compatibility.
- Add pre-merge checks as part of the CI/CD pipeline.
- Increase code coverage to test more functions.

---

## 🐶 Dog API Tests

The Dog API tests utilise the [requests](https://requests.readthedocs.io/en/latest/) library for Python to interact with the Dog API.

Explore the [Dog API](https://dog.ceo/dog-api/) that's being tested.

### ▶ Running API Tests

To run the API tests, use the following command:

```bash
poetry run pytest dog_api/tests/test_dog_facts.py
```

### Test Coverage

| Test Name        | Validation  | Reason                   |
|------------------|-------------|--------------------------|
| test_status_code | status 200  | everything is OK         |
| test_status      | success     | response is successful   |
| test_header      | data type   | is in a usable format    |
|                  | data length | data is present          |     
|                  | encoding    | data security            |
| test_message     | data values | correct data is present  |


### 🔮 Future improvements

- Increase coverage for negative test paths, ensuring bad requests (e.g., invalid inputs, missing data, unauthorized requests) are handled correctly.
- Validate that appropriate HTTP status codes (400, 401, 404, etc.) and error messages are returned for invalid or incomplete requests.
