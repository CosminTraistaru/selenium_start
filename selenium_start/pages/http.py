from selenium.webdriver.common.by import By

from .basepage import BasePage


class Http(BasePage):

    def __init__(self, selenium, variables, open_url=False):
        suffix_url = '/en-US/docs/Web/HTTP'
        super().__init__(selenium, variables, open_url, suffix_url)

    _title_header_locator = (By.TAG_NAME, 'h1')
    _edit_page_button_locator = (By.CLASS_NAME, 'page-buttons-edit')
    _http_page_title = 'HTTP'

    def confirm_page_load(self):
        self.text_is_present_in_element(
            self._title_header_locator,
            self._http_page_title)

    def edit_button_is_enabled(self):
        return self.check_clickable(
            self._edit_page_button_locator)
