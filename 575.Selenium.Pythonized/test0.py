from selenium import webdriver
import time 

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input4 = browser.find_element_by_id("country")

finally:
    # time.sleep(10)
    browser.quit()
