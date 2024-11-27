import random
from time import sleep
from setup import utils


class APYCalculator:
    def __init__(self, driver):
        self.driver = driver

    def apy_calculator_operations(self):

        locators = utils.load_locators("APYCalculator")

        principal = utils.get_random_number(1000, 100000)
        rate = utils.get_random_number(5, 16)
        years = random.choice([5, 7, 10, 12, 15])
        months = random.choice(range(1, 12))

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateAPY'])

        utils.fill_input(self.driver, locators['Principal'], principal)
        utils.fill_input(self.driver, locators['apypercent'], rate)
        utils.fill_input(self.driver, locators['Years'], years)
        utils.fill_input(self.driver, locators['Months'], months)
        utils.random_wait()

        utils.calculate_button(self.driver, locators['CalculateAPY'])

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
