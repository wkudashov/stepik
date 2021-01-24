import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

lessons = [
    "236895",
    "236896",
    "236897",
    "236898",
    "236899",
    "236903",
    "236904",
    "236905"
]

feed = []

@pytest.fixture()
def browser():
    # print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    # browser = webdriver.Chrome()
    yield browser
    # print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson', lessons)
def test_guest_should_see_login_link(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    area = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )
    button = browser.find_element_by_css_selector("button.submit-submission")
    area.send_keys(str(math.log(int(time.time()))))
    button.click()
    feedback = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div pre"))
    )

    assert feedback.text == "Correct!", f"lesson {lesson} feedback is {feedback.text}"
