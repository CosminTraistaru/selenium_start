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

    def __init__(self, driver, variables, open_url=False):
        self.driver = driver
        self.variables = variables
        if open_url:
            self.driver.get(self.variables['url'])
        self.confirm_page_load()

    def confirm_page_load(self):
        """
        In order to make sure that we are on the correct page, we can
        overwrite this method and search for a specific element for each page.
        """
        pass

    def is_visible(self, selector):
        element = WebDriverWait(self.driver, self._IMPLICIT_WAIT).until(
            ec.visibility_of_element_located(
                selector
            )
        )
        return element

    def get_element(self, selector):
        element = WebDriverWait(self.driver, self._IMPLICIT_WAIT).until(
            ec.presence_of_element_located(
                selector
            )
        )
        return element

    def get_elements(self, selector):
        elements = WebDriverWait(self.driver, self._IMPLICIT_WAIT).until(
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
        element = WebDriverWait(self.driver, self._IMPLICIT_WAIT).until(
            ec.element_to_be_clickable(
                selector
            )
        )
        element.click()

    def check_clickable(self, selector):
        WebDriverWait(self.driver, self._IMPLICIT_WAIT).until(
            ec.element_to_be_clickable(
                selector
            )
        )

    def select_text_from_dropdown(self, selector, value):
        dropdown = WebDriverWait(self.driver, self._IMPLICIT_WAIT).until(
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
        ActionChains(self.driver).\
            send_keys(keys[key]).\
            perform()
