import time
import unittest
from selenium import webdriver


class TestSel(unittest.TestCase):
    def test_reg1(self):
        try: 
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element_by_css_selector(".first_block .first")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector(".first_block .second")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector(".first_block .third")
            input3.send_keys("any@email.ru")

            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration1 failed")
            print('assert отправлен')
        finally:
            print('exiting')
            browser.quit()

    def test_reg2(self):
        try: 
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element_by_css_selector(".first_block .first")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector(".first_block .second")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector(".first_block .third")
            input3.send_keys("any@email.ru")

            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration2 failed")
            print('assert отправлен')
        finally:
            print('exiting')
            browser.quit()


if __name__ == "__main__":
    unittest.main()
