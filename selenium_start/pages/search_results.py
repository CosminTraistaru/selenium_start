from .basepage import BasePage

from selenium.webdriver.common.by import By


class SearchResultsPage(BasePage):

    _second_result = (By.CSS_SELECTOR, '.result-2 a')
    _results = (By.ID, 'search-results-close-container')

    def confirm_page_load(self):
        self.get_element(self._results)

    def click_second_result(self):
        self.click(self._second_result)
