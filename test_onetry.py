from selenium import webdriver
import time
import unittest



class test_onetry(unittest.TestCase):
    def test_onetry_one(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

    # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector("[class=first_block]>[class]:nth-child(1)>[class]")
            input1.send_keys("Дмитрий")
            input2 = browser.find_element_by_css_selector("[class=first_block]>[class]:nth-child(2)>[class]")
            input2.send_keys("Косячный")
            input3 = browser.find_element_by_css_selector("[class=first_block]>[class]:nth-child(3)>[class]")
            input3.send_keys("123@123.ru")

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
            assert "Congratulations! You have successfully registered!" == welcome_text
        finally:
           time.sleep(10)
            # закрываем браузер после всех манипуляций
           browser.quit()

    def test_onetry_two(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

    # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector('[class=first_block]>[class]:nth-child(1)>[class]')
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector('[class=first_block]>[class]:nth-child(2)>[class]')
            input2.send_keys("123@123.ru")
            input3 = browser.find_element_by_css_selector("[class=second_block]>[class]:nth-child(1)>[class]")
            input3.send_keys("7900000911")
            input4 = browser.find_element_by_css_selector('[class=second_block]>[class]:nth-child(2)>[class]')
            input4.send_keys("Russia")
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

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
            assert "Congratulations! You have successfully registered!" == welcome_text
        finally:
           time.sleep(10)
            # закрываем браузер после всех манипуляций
           browser.quit()
