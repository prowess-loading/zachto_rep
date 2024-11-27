import random
from time import sleep
from setup import utils


class SalaryToHourlyCalculator:
    def __init__(self, driver):
        self.driver = driver

    def salary_to_hourly_calculator_operations(self):
        locators = utils.load_locators("SalaryToHourlyCalculator")
        interval = random.choice(
            ['annually', 'monthly', 'biweekly', 'weekly', 'daily'])
        salary = utils.get_random_number(15000, 800000)
        week = utils.get_random_number(30, 55)
        year = utils.get_random_number(48, 52)

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateSalary'])

        utils.select_dropdown(
            self.driver, locators['salaryFrequency'], interval)
        utils.fill_input(self.driver, locators['salaryamount'], salary)
        utils.fill_input(self.driver, locators['hoursPerWeek'], week)
        utils.fill_input(self.driver, locators['weeksPerYear'], year)
        utils.random_wait()

        utils.calculate_button(self.driver, locators['CalculateSalary'])

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
