link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

    """Можно задать значение параметра по умолчанию, чтобы в
     командной строке не обязательно было указывать параметр --browser_name, 
     например, так:

parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
Давайте укажем параметр:

pytest -s -v --browser_name=chrome test_parser.py"""