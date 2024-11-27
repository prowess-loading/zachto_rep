import random
from time import sleep
from setup import utils


class MarginCalculator:
    def __init__(self, driver):
        self.driver = driver

    def margin_calculator_operations(self):
        locators = utils.load_locators("MarginCalculator")
        cost = utils.get_random_number(10000, 1000000)
        revenue = utils.get_random_number(cost, 1000000)

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateTypeWise'])

        utils.fill_input(self.driver, locators['cost'], cost)
        utils.fill_input(self.driver, locators['revenue'], revenue)
        utils.random_wait()

        utils.calculate_button(self.driver, locators['CalculateTypeWise'])

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
