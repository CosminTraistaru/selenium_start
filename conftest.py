import os

import pytest

from pyvirtualdisplay import Display


_IMPLICIT_WAIT = 20
SCREEN_RESOLUTION = (1600, 900)

env = os.getenv('TRAVIS', None)

if env:
    display = Display(visible=0, size=SCREEN_RESOLUTION)
    display.start()



@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--headless')
    return chrome_options


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(_IMPLICIT_WAIT)
    return selenium
