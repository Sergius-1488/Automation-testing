import time
from selenium import webdriver
import math
answer = math.log(int(time.time()))
print(answer)
driver = webdriver.Chrome()
driver.get("https://stepik.org/lesson/236895/step/1")


# print(answer)
driver.implicitly_wait(10)
input = driver.find_element_by_css_selector(".textarea")
input.send_keys(str(answer))
driver.find_element_by_class_name("submit-submission").click()

driver.implicitly_wait(10)
texti=driver.find_element_by_class_name("smart-hints__hint")
assert "Correct!"  in texti.text
print(texti.text)
driver.quit()
