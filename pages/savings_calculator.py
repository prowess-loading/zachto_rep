import random
from time import sleep
from setup import utils


class SavingsCalculator:
    def __init__(self, driver):
        self.driver = driver

    def savings_calculator_operations(self):

        locators = utils.load_locators("SavingsCalculator")
        init_saving = utils.get_random_number(10000, 1000000)
        interestRest = utils.get_random_number(5, 16)
        interval = random.choice(['yearly', 'monthly'])
        years = random.choice(range(0, 3))
        months = random.choice(range(1, 12))

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateSavings'])
        utils.fill_input(self.driver, locators['initialDeposit'], init_saving)
        utils.fill_input(self.driver, locators['interestRate'], interestRest)
        utils.select_dropdown(self.driver, locators['interestFreq'], interval)
        utils.fill_input(self.driver, locators['Years'], years)
        utils.fill_input(self.driver, locators['Months'], months)
        utils.random_wait()

        utils.calculate_button(self.driver, locators['CalculateSavings'])
        utils.random_wait()

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
