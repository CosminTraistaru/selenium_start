from .basepage import BasePage
from .search_results import SearchResultsPage

from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    _search_input = (By.ID, 'home-q')
    _expect_title = 'MDN Web Docs'

    def confirm_page_load(self):
        assert self.driver.title == self._expect_title

    def search(self, text):
        self.enter_text(self._search_input, text=text)
        self.send_key_press(key='ENTER')
        return SearchResultsPage(self.driver, self.variables)
