from selenium import webdriver
import math
import time

start_time=time.time()

driver=webdriver.Chrome()
driver.get('http://suninjuly.github.io/redirect_accept.html')

button= driver.find_element_by_tag_name('button').click()

win_name=driver.window_handles[1]
driver.switch_to.window(win_name)

x=driver.find_element_by_id('input_value').text

def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

result= func(x)

input=driver.find_element_by_tag_name('input').send_keys(result)

last_button = driver.find_element_by_tag_name('button').click()


alert_2=driver.switch_to.alert
print(alert_2.text)

print((time.time())-start_time,'seconds')

driver.quit()

