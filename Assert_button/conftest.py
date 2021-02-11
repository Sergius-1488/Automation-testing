import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
        parser.addoption("--language", default="ru")#, action='store', default=None, )


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    user_language=request.config.getoption("language")
    # user_language=None
    print(user_language)
    options = Options()
    options.add_experimental_option('prefs',{'intl.accept_languages': user_language})  #'es'}) #сюда запихнуть выбранный язык 
    driver = webdriver.Chrome(options=options)
    yield driver
    time.sleep(30)
    print("\nquit browser..")
    driver.quit()
