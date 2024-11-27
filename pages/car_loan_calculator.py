from time import sleep
from setup import utils
import random


class CarLoanCalculator:
    def __init__(self, driver):
        self.driver = driver

    def car_loan_calculator_operations(self):

        locators = utils.load_locators("CarLoanCalculator")
        car_value = utils.get_random_number(5000, 100000)
        rate = utils.get_random_number(5, 16)
        years = random.choice([5, 7, 10, 12, 15])
        months = random.choice(range(1, 12))
        deposit = int(car_value / utils.get_random_number(58, 79))

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateButton'])
        utils.fill_input(self.driver, locators['CarValue'], car_value)
        utils.fill_input(self.driver, locators['InterestRate'], rate)
        utils.fill_input(self.driver, locators['Years'], years)
        utils.fill_input(self.driver, locators['Months'], months)
        utils.fill_input(self.driver, locators['downpayment'], deposit)

        utils.calculate_button(self.driver, locators['CalculateButton'])
        utils.scroll_to_single(self.driver, locators['pieChart'])

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
