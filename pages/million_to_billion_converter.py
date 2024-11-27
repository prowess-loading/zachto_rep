import random
from time import sleep
from setup import utils


class MillionToBillionConverter:
    def __init__(self, driver):
        self.driver = driver

    def million_to_billion_converter_operations(self):
        locators = utils.load_locators("MillionToBillionConverter")
        amount = utils.get_random_number(10000, 1000000)

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['ConvertBtn'])
        utils.fill_input(self.driver, locators['amount'], amount)
        utils.select_dropdown(self.driver, locators['unit'], "Billion")
        utils.random_wait()

        utils.calculate_button(self.driver, locators['ConvertBtn'])

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
