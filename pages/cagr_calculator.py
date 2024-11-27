import random
from time import sleep
from setup import utils


class CAGRCalculator:
    def __init__(self, driver):
        self.driver = driver

    def cagr_calculator_operations(self):

        locators = utils.load_locators("CAGRCalculator")
        start_value = utils.get_random_number(10000, 1000000)
        end_value = utils.get_random_number(start_value, 1000000)
        years = random.choice([5, 7, 10, 12, 15])
        months = random.choice(range(1, 12))
        days = random.choice(range(1, 31))

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateCAGR'])
        utils.fill_input(self.driver, locators['initialValue'], start_value)
        utils.fill_input(self.driver, locators['finalValue'], end_value)
        utils.fill_input(self.driver, locators['years'], years)
        utils.fill_input(self.driver, locators['months'], months)
        utils.fill_input(self.driver, locators['days'], days)
        utils.random_wait()

        utils.calculate_button(self.driver, locators['CalculateCAGR'])

        utils.random_wait()

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
