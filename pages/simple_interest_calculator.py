import random
from time import sleep
from setup import utils


class SimpleInterestCalculator:
    def __init__(self, driver):
        self.driver = driver

    def simple_interest_calculator_operations(self):
        locators = utils.load_locators("SimpleInterestCalculator")

        start_balance = utils.get_random_number(10000, 1000000)
        rate = utils.get_random_number(5, 16)
        years = random.choice(range(0, 3))
        months = random.choice(range(1, 12))
        weeks = random.choice(range(1, 52))
        days = random.choice(range(1, 31))

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateButton'])
        utils.fill_input(self.driver, locators['Principal'], start_balance)
        utils.fill_input(self.driver, locators['Rate'], rate)
        utils.fill_input(self.driver, locators['Years'], years)
        utils.fill_input(self.driver, locators['Months'], months)
        utils.fill_input(self.driver, locators['Weeks'], weeks)
        utils.fill_input(self.driver, locators['Days'], days)
        utils.random_wait()

        utils.calculate_button(self.driver, locators['CalculateButton'])
        utils.random_wait()

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
