from .basepage import BasePage
from .search_results import SearchResultsPage
from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    _search_input = (By.ID, 'twotabsearchtextbox')
    _search_button = (By.CSS_SELECTOR, '.nav-search-submit')
    _expect_title = 'Amazon.com: Online Shopping for Electronics, ' \
                    'Apparel, Computers, Books, DVDs & more'

    def confirm_page_load(self):
        assert self.selenium.title == self._expect_title

    def search(self, text):
        self.enter_text(self._search_input, text=text)
        self.click(self._search_button)
        return SearchResultsPage(self.selenium, self.variables)
