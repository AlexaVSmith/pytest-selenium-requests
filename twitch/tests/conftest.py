from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element(driver, xpath):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))


def click_xpath(driver, xpath):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    ).click()


def emulator():
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
        "clientHints": {"platform": "Android", "mobile": True},
    }
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def rejects_cookies(driver):
    reject_cookies = '//*[@id="root"]/div[4]/div/div/div/div[3]/div[3]/button'
    click_xpath(driver, reject_cookies)


def browse(driver):
    browse = '//*[@id="root"]/div[2]/a[2]/div/div[2]'
    click_xpath(driver, browse)


def search(driver, search_term):
    search_field = '//*[@id="twilight-sticky-header-root"]/div/div/div/div/input'
    search = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, search_field))
    )
    search.send_keys(search_term)


def click_partial_text(driver, option):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, option))
    ).click()


def capture_screenshot(driver):
    wait_for_element(
        driver,
        '//*[@id="channel-live-overlay"]/div/div/div[2]/div[1]/div[3]/div/div/section/div/div[5]/div/div/div/div[2]/div/div/button',
    )
    driver.get_screenshot_as_file("screenshots/screenshot.png")


def scroll(driver):
    driver.execute_script("window.scrollTo(0, 300)")
