import unittest
import time

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options


class TestRegistration(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        self.browser = browser

    def tearDown(self):
        self.browser.quit()
    
    def test_registration(self):
        browser = self.browser
        urls = [
            "http://suninjuly.github.io/registration1.html",
            "http://suninjuly.github.io/registration2.html",
        ]
        for url in urls:
            with self.subTest(url=url):
                browser.get(url)
                # Ваш код, который заполняет обязательные поля
                browser.find_element_by_css_selector(".first_block .first").send_keys("First Name")
                browser.find_element_by_css_selector(".first_block .second").send_keys("Second Name")
                browser.find_element_by_css_selector(".first_block .third").send_keys("Email")

                # Отправляем заполненную форму
                button = browser.find_element_by_css_selector("button.btn")
                button.click()

                # Проверяем, что смогли зарегистрироваться
                # ждем загрузки страницы
                time.sleep(1)

                # находим элемент, содержащий текст
                welcome_text_elt = browser.find_element_by_tag_name("h1")
                # записываем в переменную welcome_text текст из элемента welcome_text_elt
                welcome_text = welcome_text_elt.text
                self.assertTrue("Congratulations! You have successfully registered!" == welcome_text)

if __name__ == "__main__":
    unittest.main()