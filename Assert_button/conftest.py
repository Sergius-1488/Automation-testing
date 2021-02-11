import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", default="ru")#, action='store', default=None, )


@pytest.fixture(scope="function")
def browser(request):
    user_language=request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs',{'intl.accept_languages': user_language})  #'es'}) #сюда запихнуть выбранный язык 
    print("\nstart browser for test..")
    driver = webdriver.Chrome(options=options)
    time.sleep(5)
    yield driver
    print("\nquit browser..")
    driver.quit()
