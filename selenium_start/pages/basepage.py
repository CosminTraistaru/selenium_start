""" Basic page actions, this is a wrapper over selenium calls. """

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    In this class there are defined all the basic page interactions.
    Like click, enter text, select from drop down. And also all the selenium
    calls. I try to not have any selenium calls in other modules.
    """

    _IMPLICIT_WAIT = 20

    def __init__(self, selenium, variables, open_url=False):
        self.selenium = selenium
        self.variables = variables
        self.selenium.implicitly_wait = self._IMPLICIT_WAIT
        if open_url:
            self.selenium.get(self.variables['url'])
        self.confirm_page_load()

    def confirm_page_load(self):
        """
        In order to make sure that we are on the correct page, we can
        overwrite this method and search for a specific element for each page.
        """
        pass

    def is_visible(self, selector):
        element = WebDriverWait(self.selenium, self._IMPLICIT_WAIT).until(
            ec.visibility_of_element_located(
                selector
            )
        )
        return element

    def get_element(self, selector):
        element = WebDriverWait(self.selenium, self._IMPLICIT_WAIT).until(
            ec.presence_of_element_located(
                selector
            )
        )
        return element

    def get_elements(self, selector):
        elements = WebDriverWait(self.selenium, self._IMPLICIT_WAIT).until(
            ec.presence_of_all_elements_located(
                selector
            )
        )
        return elements

    def enter_text(self, selector, text):
        element = self.is_visible(selector)
        element.click()
        element.clear()
        element.send_keys(text)

    def click(self, selector):
        element = WebDriverWait(self.selenium, self._IMPLICIT_WAIT).until(
            ec.element_to_be_clickable(
                selector
            )
        )
        element.click()

    def check_clickable(self, selector):
        WebDriverWait(self.selenium, self._IMPLICIT_WAIT).until(
            ec.element_to_be_clickable(
                selector
            )
        )

    def select_text_from_dropdown(self, selector, value):
        dropdown = WebDriverWait(self.selenium, self._IMPLICIT_WAIT).until(
            ec.visibility_of_element_located(selector)
        )
        Select(dropdown).select_by_value(value)

    def send_key_press(self, key='ENTER'):
        keys = {
            'ENTER': Keys.ENTER,
            'TAB': Keys.TAB,
            'SPACE': Keys.SPACE,
            'RIGHT': Keys.RIGHT
        }
        ActionChains(self.selenium).\
            send_keys(keys[key]).\
            perform()

    def hover(self, selector):
        element = self.get_element(selector)
        hover = ActionChains(self.selenium).move_to_element(element)
        hover.perform()

    def drag_and_drop(self, src_selector, dest_selector):
        source = self.get_element(src_selector)
        destination = self.get_element(dest_selector)
        drag = ActionChains(self.selenium).drag_and_drop(source, destination)
        drag.perform()
