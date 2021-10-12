import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="browser language")


@pytest.fixture
def browser(request):
    browser_language = request.config.getoption("language")
    options = Options()
    options.add_argument("--window-position=0,0")
    options.add_argument("--headless")
    options.add_experimental_option('prefs', {"intl.accept_languages": browser_language})
    if browser_language:
        print(f"\nusing browser language: {browser_language}")
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
    else:
        raise pytest.UsageError("missing required parameter: --language")
    yield browser
    print("\nbrowser quit")
    browser.quit()
