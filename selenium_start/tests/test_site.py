from selenium_start.pages.landing import LandingPage
from selenium_start.pages.header import Header
from selenium_start.pages.http import Http


def test_navigate_to_http_page(selenium, variables):
    LandingPage(selenium, variables, open_url=True)
    header = Header(selenium, variables)
    http = header.navigate_to_http_page()
    assert http.edit_button_is_enabled()


def test_edit_button_is_enabled_on_http_page(selenium, variables):
    http = Http(selenium, variables, open_url=True)
    assert http.edit_button_is_enabled()
