from .basepage import BasePage
from .search_results import SearchResultsPage
from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    _search_input = (By.ID, 'emg-input-autosuggest')
    _search_button = (By.ID, 'emg-category-menu-icon')
    expect_title = 'eMAG.ro - cea mai variata gama de produse'

    def confirm_page_load(self):
        assert self.selenium.title == self.expect_title

    def search(self, text):
        self.enter_text(self._search_input, text=text)
        self.click(self._search_button)
        return SearchResultsPage(self.selenium, self.variables)
