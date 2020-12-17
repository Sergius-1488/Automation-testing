from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/selects2.html')

num_1 = driver.find_element_by_id('num1').text

num_2 = driver.find_element_by_id('num2').text


def sum(num_1, num_2):
    return str(int(num_1) + int(num_2))

result = (sum(num_1, num_2))

select = Select(driver.find_element_by_tag_name('select'))
select.select_by_value(result)

button = driver.find_element_by_tag_name('button').click()

alert = driver.switch_to_alert()
print(alert.text)

driver.quit()
