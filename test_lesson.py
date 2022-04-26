import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link1 = "https://stepik.org/lesson/236895/step/1"
link2 = "https://stepik.org/lesson/236896/step/1"
link3 = "https://stepik.org/lesson/236897/step/1"
link4 = "https://stepik.org/lesson/236898/step/1"
link5 = "https://stepik.org/lesson/236899/step/1"
link6 = "https://stepik.org/lesson/236903/step/1"
link7 = "https://stepik.org/lesson/236904/step/1"
link8 = "https://stepik.org/lesson/236905/step/1"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    return browser


class TestAnswer1:
    def test_answer1_link(self, browser):
        browser.get(link1)
        text = browser.find_element(By.TAG_NAME, value='textarea')
        answer = math.log(int(time.time()))
        text.send_keys(answer)
        button = browser.find_element(By.CLASS_NAME, value='submit-submission')
        button.click()
        time.sleep(10)


class TestAnswer2:
    def test_answer2_link(self, browser):
        browser.get(link2)
        text = browser.find_element(By.TAG_NAME, value='textarea')
        answer = math.log(int(time.time()))
        text.send_keys(answer)
        button = browser.find_element(By.CLASS_NAME, value='submit-submission')
        button.click()
        time.sleep(10)


class TestAnswer3:
    def test_answer3_link(self, browser):
        browser.get(link3)
        text = browser.find_element(By.TAG_NAME, value='textarea')
        answer = math.log(int(time.time()))
        text.send_keys(answer)
        button = browser.find_element(By.CLASS_NAME, value='submit-submission')
        button.click()
        time.sleep(10)


class TestAnswer4:
    def test_answer4_link(self, browser):
        browser.get(link4)
        text = browser.find_element(By.TAG_NAME, value='textarea')
        answer = math.log(int(time.time()))
        text.send_keys(answer)
        button = browser.find_element(By.CLASS_NAME, value='submit-submission')
        button.click()
        time.sleep(10)


class TestAnswer5:
    def test_answer5_link(self, browser):
        browser.get(link5)
        text = browser.find_element(By.TAG_NAME, value='textarea')
        answer = math.log(int(time.time()))
        text.send_keys(answer)
        button = browser.find_element(By.CLASS_NAME, value='submit-submission')
        button.click()
        time.sleep(10)


class TestAnswer6:
    def test_answer6_link(self, browser):
        browser.get(link6)
        text = browser.find_element(By.TAG_NAME, value='textarea')
        answer = math.log(int(time.time()))
        text.send_keys(answer)
        button = browser.find_element(By.CLASS_NAME, value='submit-submission')
        button.click()
        time.sleep(10)


class TestAnswer7:
    def test_answer7_link(self, browser):
        browser.get(link7)
        text = browser.find_element(By.TAG_NAME, value='textarea')
        answer = math.log(int(time.time()))
        text.send_keys(answer)
        button = browser.find_element(By.CLASS_NAME, value='submit-submission')
        button.click()
        time.sleep(10)


class TestAnswer8:
    def test_answer8_link(self, browser):
        browser.get(link8)
        text = browser.find_element(By.TAG_NAME, value='textarea')
        answer = math.log(int(time.time()))
        text.send_keys(answer)
        button = browser.find_element(By.CLASS_NAME, value='submit-submission')
        button.click()
        time.sleep(10)
