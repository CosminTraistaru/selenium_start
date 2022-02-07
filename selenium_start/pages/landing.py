""" Page Object Class for the landing page for Mozilla Developers site"""

from selenium.webdriver.common.by import By

from .basepage import BasePage
from .search_results import SearchResultsPage


class LandingPage(BasePage):
    _search_input = (By.ID, 'main-q')
    _result_item = (By.CLASS_NAME, 'result-item ')
    _expect_title = 'MDN Web Docs'

    def confirm_page_load(self):
        assert self.selenium.title == self._expect_title

    def search(self, text):
        self.enter_text(self._search_input, text=text)
        self.get_element(self._result_item)
        return SearchResultsPage(self.selenium, self.variables)
