import pytest

from selenium_start.pages.landing import LandingPage


def test_mozilla_search(driver, variables):
    landing_page = LandingPage(driver, variables, open_url=True)
    landing_page.search('firefox')
    assert driver.title == 'Search Results for "firefox" | MDN'


def test_mozilla_search_2(driver, variables):
    landing_page = LandingPage(driver, variables, open_url=True)
    landing_page.search('firefox')
    assert driver.title == 'Search Results for "firefox" | MDN'


def test_mozilla_search_3(driver, variables):
    landing_page = LandingPage(driver, variables, open_url=True)
    landing_page.search('firefox')
    assert driver.title == 'Search Results for "firefox" | MDN'


@pytest.mark.xfail
def test_mozilla_search_fail(driver, variables):
    landing_page = LandingPage(driver, variables, open_url=True)
    search_results = landing_page.search('security')
    search_results.click_second_result()
    assert 'caca' in driver.title
