from selenium import webdriver
import math
import time

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/execute_script.html')
x = driver.find_element_by_id('input_value').text
print(x)


def res(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


result = res(x)
print(result)
input = driver.find_element_by_id('answer')
input.send_keys(result)

check_box = driver.find_element_by_id('robotCheckbox').click()

# driver.execute_script('windows.scrollBy(0, 100;') '''проскролить страницу на 100 рх вниз'''

radiobutton = driver.find_element_by_id('robotsRule')
driver.execute_script('return arguments[0].scrollIntoView(true);', radiobutton)
radiobutton.click()

button = driver.find_element_by_tag_name('button').click()

time.sleep(3)

alert = driver.switch_to_alert()
print(alert.text)

driver.quit()
