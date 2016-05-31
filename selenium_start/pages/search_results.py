from .basepage import BasePage

from selenium.webdriver.common.by import By


class SearchResultsPage(BasePage):

    products = (By.CSS_SELECTOR, '.product-holder-grid .middle-container')

    def click_second_product(self):
        products = self.get_elements(self.products)
        products[1].click()
