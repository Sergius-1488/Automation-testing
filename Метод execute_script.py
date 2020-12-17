from selenium import webdriver
import time
browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")  #выскакивающее сообщение на странице
# browser.execute_script("document.title='Script executing';") #сообщение в названии страницы
browser.execute_script("document.title='Script executing';alert('Robots at work');") #Сообщение в
# названии страницы и в предупреждении

time.sleep(10)

browser.quit()
