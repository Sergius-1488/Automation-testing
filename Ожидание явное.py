from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

start_time=time.time()
driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/explicit_wait2.html')

book = WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100") #ожидание появления цифры 100
    )
driver.find_element_by_id('book').click()#нажатие кнопки

x=driver.find_element_by_id('input_value').text

def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

result= func(x)

input=driver.find_element_by_tag_name('input').send_keys(result)

button = WebDriverWait(driver,3).until(
    EC.element_to_be_clickable((By.ID, 'solve')) #ожидаем, когда кнопка станет активной
)
button.click()


alert=driver.switch_to.alert
print(alert.text)
alert.accept()

print((time.time())-start_time,'seconds')


driver.quit()
