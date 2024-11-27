from time import sleep
from setup import utils


class LoanPayoffCalculator:
    def __init__(self, driver):
        self.driver = driver

    def loan_payoff_calculator_operations(self):

        locators = utils.load_locators("LoanPayoffCalculator")
        loan_balance = utils.get_random_number(10000, 10000000)
        rate = utils.get_random_number(5, 16)
        addition = int(loan_balance / utils.get_random_number(35, 68))

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateButton'])
        utils.fill_input(self.driver, locators['LoanBalance'], loan_balance)
        utils.fill_input(self.driver, locators['rate'], rate)
        utils.fill_input(self.driver, locators['addition'], addition)
        utils.random_wait()

        utils.calculate_button(self.driver, locators['CalculateButton'])
        utils.random_wait()

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
