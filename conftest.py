import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as chrome_options


# @pytest.fixture
# def fixture_for_set_params():
#     options = chrome_options()
#     options.add_argument('chrome')
#     options.add_argument('--start-maximized')
#     options.add_argument('--headless')
#     return options


@pytest.fixture
def fixture_for_set_driver():
    # options = fixture_for_set_params
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    return driver


@pytest.fixture(scope='function')
def setup(fixture_for_set_driver):
    driver = fixture_for_set_driver
    url = 'https://cyberleninka.ru/article/c/civil-engineering'
    driver.get(url)
    yield driver
    driver.quit()
