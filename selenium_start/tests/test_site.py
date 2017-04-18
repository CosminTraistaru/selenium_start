import pytest

from selenium_start.pages.landing import LandingPage


def test_mozilla_search(selenium, variables):
    landing_page = LandingPage(selenium, variables, open_url=True)
    landing_page.search('firefox')
    assert selenium.title == 'Search Results for "firefox" | MDN'


@pytest.mark.xfail
def test_mozilla_search_fail(selenium, variables):
    landing_page = LandingPage(selenium, variables, open_url=True)
    search_results = landing_page.search('aer conditionat')
    search_results.click_second_result()
    assert 'caca' in selenium.title
