import random
from time import sleep
from setup import utils


class PricePerSquareFeetCalculator:
    def __init__(self, driver):
        self.driver = driver

    def price_per_sqft_converter_operations(self):
        locators = utils.load_locators("PricePerSquareFeetCalculator")
        price = utils.get_random_number(10000, 1000000)
        area = utils.get_random_number(200, 3500)
        interval = random.choice(['sqft', 'sqm', 'sqyd'])

        utils.select_random_currency(self.driver, locators)
        utils.scroll_to_calculate_button(
            self.driver, locators['CalculateArea'])
        utils.fill_input(self.driver, locators['totalPrice'], price)
        utils.fill_input(self.driver, locators['totalarea'], area)
        utils.select_dropdown(self.driver, locators['areaUnit'], interval)
        utils.random_wait()

        utils.calculate_button(self.driver, locators['CalculateArea'])

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
