import pytest

from pyvirtualdisplay import Display


_IMPLICIT_WAIT = 20

display = Display(visible=0, size=(1600, 900))
display.start()


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(_IMPLICIT_WAIT)
    # selenium.maximize_window()  # chromedriver bug
    return selenium
