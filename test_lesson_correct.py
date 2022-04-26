import pytest
from selenium import webdriver
import time
import math

magic = []  # Задание переменной для сбора значений из неверных опциональных фидбеков


@pytest.fixture(scope="function")  # задание фикстуры для открытия и закрытия браузера при выполнении теста
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('sites', ["236895", "236896", "236897", "236898", "236899", "236903", "236904",
                                   "236905"])  # задание фикстуры с параметром для открытия нескольких ссылок
class TestLinks:
    def test_links(self, browser, sites):
        link = f"https://stepik.org/lesson/{sites}/step/1"  # ссылка для открытия
        browser.get(link)
        browser.implicitly_wait(
            5)  # задержка перед прохождением теста необходима, чтобы загрузилось содержимое страницы
        input1 = browser.find_element_by_css_selector(".textarea")  # находим на странице элемент для ввода текста
        answer = (math.log(int(time.time())))  # рассчитываем время открытия сайта
        otvet = str(answer)  # переводим полученное значение из численного в строковое
        input1.send_keys(otvet)  # вставляем в поле ответа
        button1 = browser.find_element_by_class_name("submit-submission")  # ищем кнопку для отправки ответа на странице
        button1.click()  # нажимаем кнопку
        actual_result = browser.find_element_by_class_name(
            "smart-hints__hint").text  # сравниваем полученный результат в опциональном фидбеке с ожидаемым
        # assert actual_result== "Correct!",\
        # f"Wrong optional text, got: {actual_result} instead of 'Correct!' "
        if actual_result != "Correct!":  # если результаты не совпадают, то тогда значение из опционального фидбека добавляется в переменную magic
            magic.append(actual_result)
        print("".join(magic))  # вывод фразы из всех полученных неверных значений опциональных фидбеков