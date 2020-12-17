from selenium import webdriver
import math
import time

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/math.html')
x_element = driver.find_element_by_css_selector('span[id="input_value"]')
x = x_element.text
print(x)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


answer = calc(x)
print(answer)
input1 = driver.find_element_by_xpath("//input[@id='answer']")
input1.send_keys(answer)

check_box = driver.find_element_by_xpath('//body/div[1]/form[1]/div[2]/label[1]')
check_box.click()


radio=driver.find_element_by_css_selector('label[for="robotsRule"]')
radio.click()

button=driver.find_element_by_tag_name('button')
button.click()

time.sleep(10)
driver.close()
driver.quit()
