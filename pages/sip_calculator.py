import random
from time import sleep
from setup import utils


class SIPCalculator:
    def __init__(self, driver):
        self.driver = driver

    def sip_calculator_operations(self):

        freq = ["monthly", "quarterly", "halfYearly", "yearly"]

        locators = utils.load_locators("SIPCalculator")
        amount = utils.get_random_number(10000, 1000000)
        rate = utils.get_random_number(5, 16)
        years = random.choice([5, 7, 10, 12, 15])
        months = random.choice(range(1, 12))
        time_freq = random.choice(freq)

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(self.driver, locators['CalculateSIP'])

        utils.fill_input(self.driver, locators['investmentAmount'], amount)
        utils.select_dropdown(
            self.driver, locators['investmentFrequency'], time_freq)
        utils.fill_input(self.driver, locators['interestRate'], rate)
        utils.fill_input(self.driver, locators['Years'], years)
        utils.fill_input(self.driver, locators['Months'], months)
        utils.random_wait()

        utils.calculate_button(self.driver, locators['CalculateSIP'])
        utils.random_wait()
        utils.scroll_to_single(self.driver, locators['WealthGain'])

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
