""" Configuration file for pytest. """
import os

import pytest

from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

_IMPLICIT_WAIT = 20
SCREEN_RESOLUTION = (1600, 900)

if os.getenv('TRAVIS', None):
    display = Display(size=SCREEN_RESOLUTION)
    display.start()


@pytest.fixture
def selenium():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


# @pytest.fixture
# def chrome_options(chrome_options):
#     # chrome_options.add_argument('--headless')
#     return chrome_options
