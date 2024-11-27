import random
from time import sleep
from setup import utils


class LoanCalculator:
    def __init__(self, driver):
        self.driver = driver

    def loan_calculator_operations(self):
        browserName = self.driver.capabilities['browserName'].lower()

        locators = utils.load_locators("LoanCalculator")
        loan_amount = utils.get_random_number(10000, 10000000)
        rate = utils.get_random_number(5, 16)
        years = random.choice([5, 7, 10, 12, 15])
        months = random.choice(range(1, 12))

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateButton'])
        utils.fill_input(self.driver, locators['LoanAmount'], loan_amount)
        utils.fill_input(self.driver, locators['InterestRate'], rate)
        utils.fill_input(self.driver, locators['Years'], years)
        utils.fill_input(self.driver, locators['Months'], months)

        utils.calculate_button(self.driver, locators['CalculateButton'])

        utils.scroll_to_single(self.driver, locators['NoOfMonth'])
        utils.select_result(self.driver, locators['LoanSummaryChart'])

        if 'firefox' in browserName:
            for locator in ['LoanSummaryTable', 'MonthlyBreakdown', 'YearlyBreakdown']:
                utils.select_result(self.driver, locators[locator])

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
