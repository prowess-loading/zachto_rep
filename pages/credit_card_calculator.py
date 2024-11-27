from time import sleep
from setup import utils


class CreditCardCalculator:
    def __init__(self, driver):
        self.driver = driver

    def credit_card_calculator_operations(self):

        locators = utils.load_locators("CreditCardCalculator")
        cc_balance = utils.get_random_number(500, 10000)
        apr = utils.get_random_number(18, 36)
        addition = int(cc_balance / utils.get_random_number(35, 68))

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateCCRepayment'])
        utils.fill_input(self.driver, locators['Principal'], cc_balance)
        utils.fill_input(self.driver, locators['interest'], apr)
        utils.fill_input(self.driver, locators['paymonths'], addition)

        utils.calculate_button(self.driver, locators['CalculateCCRepayment'])

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
