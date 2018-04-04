from selenium.webdriver.common.by import By

from .basepage import BasePage
from .http import Http


class Header(BasePage):

    _technologies_button_locator = (By.CSS_SELECTOR, '.nav-main-item > a[href$="/docs/Web"]')
    _http_button_locator = (By.CSS_SELECTOR, '#nav-tech-submenu a[href$="/docs/Web/HTTP"]')

    def navigate_to_http_page(self):
        self.hover(self._technologies_button_locator)
        self.click(self._http_button_locator)
        return Http(self.selenium, self.variables)
