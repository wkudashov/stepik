from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    e_el = browser.find_element_by_id("input_value")
    x = e_el.text
    y = calc(x)
 
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    chkbx = browser.find_element_by_id("robotCheckbox")
    chkbx.click()
	
    rbut = browser.find_element_by_css_selector("[name='ruler'][value='robots']")
    rbut.click()
	
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()