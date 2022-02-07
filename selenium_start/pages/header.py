from selenium.webdriver.common.by import By

from .basepage import BasePage
from .http import Http


class Header(BasePage):

    _technologies_button_locator = (By.ID, 'technologies-button')
    _http_button_locator = (By.CSS_SELECTOR, '.technologies  a[href$="/docs/Web/HTML"]')

    def navigate_to_http_page(self):
        self.click(self._technologies_button_locator)
        self.click(self._http_button_locator)
        return Http(self.selenium, self.variables)
