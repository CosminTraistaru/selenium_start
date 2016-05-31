import pytest

from pyvirtualdisplay import Display


_IMPLICIT_WAIT = 20

display = Display(visible=0, size=(1366, 768))
display.start()


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(_IMPLICIT_WAIT)
    selenium.maximize_window()
    return selenium
