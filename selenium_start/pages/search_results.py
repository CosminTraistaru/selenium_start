""" Page Object Class for the search results page. """

from selenium.webdriver.common.by import By

from .basepage import BasePage


class SearchResultsPage(BasePage):

    _second_result = (By.CSS_SELECTOR, '.result-2')

    def click_second_result(self):
        self.click(self._second_result)
