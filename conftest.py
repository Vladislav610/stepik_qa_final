import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language:")

@pytest.fixture(scope="function")
def browser(request):
    language_parametr = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs',{'intl.accept_languages': language_parametr})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()