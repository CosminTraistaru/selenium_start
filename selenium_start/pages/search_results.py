""" Page Object Class for the search results page. """

from selenium.webdriver.common.by import By

from .basepage import BasePage


class SearchResultsPage(BasePage):

    _second_result = (By.CSS_SELECTOR, '.search-result-url')
    _search_results_div = (By.CLASS_NAME, 'site-search')

    def confirm_page_load(self):
        self.get_element(self._search_results_div)

    def click_second_result(self):
        self.click(self._second_result)
