from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    input = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)
	
    chkbx = browser.find_element_by_id("robotCheckbox")
    chkbx.click()
	
    rbut = browser.find_element_by_css_selector("[name='ruler'][value='robots']")
    rbut.click()

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(15)
    browser.quit()