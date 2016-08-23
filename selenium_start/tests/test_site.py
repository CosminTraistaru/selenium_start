import pytest

from selenium_start.pages.landing import LandingPage


def test_emag_search(selenium, variables):
    landing_page = LandingPage(selenium, variables, open_url=True)
    search_results = landing_page.search('nexus')
    assert selenium.title == 'Amazon.com: nexus'


@pytest.mark.xfail
def test_emag_search_fail(selenium, variables):
    landing_page = LandingPage(selenium, variables, open_url=True)
    search_results = landing_page.search('aer conditionat')
    search_results.click_second_product()
    assert 'caca' in selenium.title
