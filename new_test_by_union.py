import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
    def test_1(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://suninjuly.github.io/registration1.html')
        driver=self.driver
         # Ваш код, который заполняет обязательные поля
        first_name=driver.find_element_by_class_name('form-control.first').send_keys('Georg')
        second_name = driver.find_element_by_xpath('//body/div[1]/form[1]/div[1]/div[2]/input[1]').send_keys('Ivanoff')
        mail = driver.find_element_by_class_name('form-control.third').send_keys('ivanoff@mail.com')
    # Отправляем заполненную форму
        button = driver.find_element_by_css_selector("button.btn")
        button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(5)
    # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
    # закрываем браузер после всех манипуляций
        driver.close()
    def test_2(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://suninjuly.github.io/registration2.html')
        driver=self.driver
         # Ваш код, который заполняет обязательные поля
        first_name=driver.find_element_by_class_name('form-control.first').send_keys('Georg')
        second_name = driver.driver.find_element_by_xpath('//body/div[1]/form[1]/div[1]/div[2]/input[1]').send_keys('Ivanoff')
        mail = driver.find_element_by_class_name('form-control.third').send_keys('ivanoff@mail.com')
    # Отправляем заполненную форму
        button = driver.find_element_by_css_selector("button.btn")
        button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(5)
    # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
    # закрываем браузер после всех манипуляций
        driver.quit()


if __name__ == "__main__":
    unittest.main()
