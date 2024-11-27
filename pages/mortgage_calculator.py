import random
from time import sleep
from setup import utils


class MortgageCalculator:
    def __init__(self, driver):
        self.driver = driver

    def mortgage_calculator_operations(self):
        locators = utils.load_locators("MortgageCalculator")

        debt = utils.get_random_number(1000, 100000)
        rate = utils.get_random_number(5, 16)
        years = random.choice([5, 7, 10, 12, 15])

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateMortgage'])

        utils.fill_input(self.driver, locators['loanAmount'], debt)
        utils.fill_input(self.driver, locators['interestRate'], rate)
        utils.fill_input(self.driver, locators['Years'], years)
        utils.random_wait()

        utils.calculate_button(self.driver, locators['CalculateMortgage'])

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
