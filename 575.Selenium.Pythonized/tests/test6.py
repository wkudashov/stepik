from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element_by_css_selector("div.first_block:nth-child(1) input.form-control.first")
input1.send_keys("Юлия")
input2 = browser.find_element_by_css_selector("div.first_block:nth-child(1) input.form-control.second")
input2.send_keys("Моя")
input3 = browser.find_element_by_css_selector("div.first_block:nth-child(1) input.form-control.third")
input3.send_keys("190590")
# Проверяем, что заполнены нужные поля
time.sleep(3)
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

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
