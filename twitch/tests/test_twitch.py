import requests
from conftest import (
    emulator,
    rejects_cookies,
    browse,
    scroll,
    search,
    click_partial_text,
    click_xpath,
    capture_screenshot,
)

ENDPOINT = "https://www.twitch.tv/"
TITLE = "Twitch"
SEARCH_ID = "tw-9f8781fbb935616110808624c66c0e4f"
SEARCH_TERM = "StarCraft II"
CHANNEL = '//*[@id="page-main-content-wrapper"]/div/div/section[1]/div[4]/button/div'


def test_endpoint():
    endpoint = requests.get(ENDPOINT)
    assert endpoint.status_code == 200


def test_emulator():
    driver = emulator()
    assert "<selenium.webdriver.chrome.webdriver.WebDriver" in str(driver)


def test_twitch():
    # Sets up mobile emulator
    driver = emulator()

    # Gets Twitch endpoint
    driver.get(ENDPOINT)

    # Rejects Cookies
    rejects_cookies(driver)

    # Clicks on 'Browse'
    browse(driver)

    # Searches for 'StarCraft II'
    search(driver, SEARCH_TERM)

    # Selects by partial text
    click_partial_text(driver, SEARCH_TERM)

    # Scroll down twice
    scroll(driver)
    scroll(driver)

    # Selects a channel
    click_xpath(driver, CHANNEL)

    # Captures screenshot - sporty/twitch/screenshots
    capture_screenshot(driver)
