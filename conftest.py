import os

import pytest

from pyvirtualdisplay import Display
from selenium import webdriver


_IMPLICIT_WAIT = 20
SCREEN_RESOLUTION = (1600, 900)

env = os.getenv('TRAVIS', None)

if env:
    display = Display(visible=0, size=SCREEN_RESOLUTION)
    display.start()


def chrome_options():
    co = webdriver.ChromeOptions()
    co.add_argument('--headless')
    return co


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        choices=('firefox', 'chrome', 'edge', 'no'),
        help='Select your desired browser.'
    )


@pytest.fixture(scope='class')
def driver(request):
    """ This creates a selenium browser instance """
    browser = request.config.getoption('--browser')

    try:
        if browser == 'no':
            return
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'chrome':
            driver = webdriver.Chrome(chrome_options=chrome_options())
        elif browser == 'edge':
            driver = webdriver.Edge()
        elif browser == 'internet':
            driver = webdriver.Ie()

    except KeyError:
        raise Exception('Selenium Driver not found')

    driver.implicitly_wait(_IMPLICIT_WAIT)

    driver.set_window_size(*SCREEN_RESOLUTION)
    request.addfinalizer(driver.quit)
    yield driver
