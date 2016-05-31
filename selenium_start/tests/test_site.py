from selenium_start.pages.landing import LandingPage


def test_emag_search(selenium, variables):
    landing_page = LandingPage(selenium, variables, open_url=True)
    search_results = landing_page.search('aer conditionat')
    search_results.click_second_product()
    assert 'Aparat de aer conditionat' in selenium.title


def test_emag_search_fail(selenium, variables):
    landing_page = LandingPage(selenium, variables, open_url=True)
    search_results = landing_page.search('aer conditionat')
    search_results.click_second_product()
    assert 'caca' in selenium.title
