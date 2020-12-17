from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/file_input.html')


first_name = driver.find_element_by_css_selector('body > div > form > div > input:nth-child(2)').send_keys('Sergius')

last_name = driver.find_element_by_xpath('//input[2]').send_keys('Dou')

e_mail = driver.find_element_by_xpath('//input[3]').send_keys('mr.dou@m.ua')

download_file = driver.find_element_by_id('file')
current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к дирректории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt') # добавляем к этому пути имя файла
download_file.send_keys(file_path)

button= driver.find_element_by_tag_name('button').click()

alert = driver.switch_to.alert
print(alert.text)

# driver.close()

driver.quit()
