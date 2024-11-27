import random
from time import sleep
from setup import utils


class CompoundInterestCalculator:
    def __init__(self, driver):
        self.driver = driver

    def compound_interest_calculator_operations(self):
        browserName = self.driver.capabilities['browserName'].lower()

        locators = utils.load_locators("CompoundInterestCalculator")
        principal = utils.get_random_number(10000, 1000000)
        rate = utils.get_random_number(5, 16)
        years = random.choice([5, 7, 10, 12, 15])
        months = random.choice(range(1, 12))
        freq = random.choice(
            ['1', '2', '4', '6', '12', '24', '26', '52', '104', '360', '365'])

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateInterest'])
        utils.fill_input(self.driver, locators['Principal'], principal)
        utils.fill_input(self.driver, locators['rate'], rate)
        utils.fill_input(self.driver, locators['Years'], years)
        utils.fill_input(self.driver, locators['Months'], months)
        utils.select_dropdown(self.driver, locators['compoundFreq'], freq)
        utils.random_wait()

        utils.calculate_button(self.driver, locators['CalculateInterest'])

        utils.scroll_to_single(self.driver, locators['RoR'])
        utils.select_result(self.driver, locators['LoanSummaryChart'])

        if 'firefox' in browserName:
            for locator in ['LoanSummaryTable', 'MonthlyBreakdown', 'YearlyBreakdown']:
                utils.select_result(self.driver, locators[locator])

        # Link clicks
        # utils.link_clicks(self.driver)
        # utils.link_clicks(self.driver)

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
