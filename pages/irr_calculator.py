import random
from time import sleep
from setup import utils


class IRRCalculator:
    def __init__(self, driver):
        self.driver = driver

    def cashflow(self, amount):
        values = [str(amount + random.randint(100, 1000)) for _ in range(3)]
        return ",".join(values)

    def irr_calculator_operations(self):

        locators = utils.load_locators("IRRCalculator")
        amount = utils.get_random_number(10000, 1000000)
        cashFlow = self.cashflow(amount)

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateIRR'])

        utils.fill_input(self.driver, locators['initialAmount'], amount)
        utils.fill_input(self.driver, locators['cashFlow'], cashFlow)
        utils.random_wait()

        utils.calculate_button(self.driver, locators['CalculateIRR'])

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
