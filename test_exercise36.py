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


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1"])
def test_exercise(driver):
    link = f'{link}'
    driver.get(f'{link}')
    answer = math.log(int(time.time()))
    driver.find_element_by_id('ember98').send_keys(answer)
    driver.find_element_by_class('submit-submission').click()


