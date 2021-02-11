import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# def pytest_addoption(parser):
#         parser.addoption(
#         "--language", action="store", default="ru", help="ru"
#     )

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs',{'intl.accept_languages':'es'}) #сюда запихнуть выбранный язык 
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()






    
# @pytest.fixture
# def cmdopt(request):
#     return request.config.getoption("--language")