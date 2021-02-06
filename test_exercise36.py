import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_exercise(driver, number):
    link = f'https://stepik.org/lesson/{number}/step/1'
    driver.get(link)
    answer = math.log(int(time.time()))
    driver.implicitly_wait(10)
    input = driver.find_element_by_css_selector(".textarea")
    input.send_keys(str(answer))
    driver.find_element_by_class_name("submit-submission").click()
    driver.implicitly_wait(10)
    texti=driver.find_element_by_class_name("smart-hints__hint")
    assert "Correct!"  in texti.text
    print(texti.text)





