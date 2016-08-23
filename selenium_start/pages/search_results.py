from .basepage import BasePage

from selenium.webdriver.common.by import By


class SearchResultsPage(BasePage):

    _second_product = (By.CSS_SELECTOR, '#result_1 img')

    def click_second_product(self):
        self.click(self._second_product)
