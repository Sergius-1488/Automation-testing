from selenium import webdriver
import math

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/get_attribute.html')
chest = driver.find_element_by_tag_name('img')  # поиск элемента по тегу
x = chest.get_attribute('valuex')
print(x)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


answer = calc(x)
input = driver.find_element_by_xpath("//input[@id='answer']")
input.send_keys(answer)

check_box = driver.find_element_by_id('robotCheckbox')
check_box.click()

radio = driver.find_element_by_css_selector('#robotsRule')
radio.click()

button = driver.find_element_by_tag_name('button')
button.click()

alert = driver.switch_to.alert()
print(alert.text)

driver.quit()
