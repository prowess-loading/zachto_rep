import random
from time import sleep
from setup import utils


class CurrencyConverter:
    def __init__(self, driver):
        self.driver = driver

    def currency_converter_operations(self):

        currencies = [
            "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD",
            "NOK", "INR", "BRL", "ZAR", "RUB", "TRY", "SGD", "HKD", "MXN", "IDR",
            "MYR", "PHP", "THB", "KRW", "DKK", "PLN", "HUF", "CZK", "ILS", "CLP",
            "ARS", "EGP", "AED", "COP", "BGN", "HRK", "RON", "KWD", "QAR", "SAR"
        ]
        locators = utils.load_locators("CurrencyConverter")

        amount = utils.get_random_number(10000, 1000000)
        fromC = random.choice(currencies)
        ToC = random.choice([
            currency for currency in currencies if currency != fromC])

        utils.scroll_to_calculate_button(
            self.driver, locators['ConvertBtn'])
        utils.fill_input(self.driver, locators['amount'], amount)
        utils.select_dropdown(self.driver, locators['from'], fromC)
        sleep(1)
        utils.select_dropdown(self.driver, locators['to'], ToC)
        utils.random_wait()

        utils.calculate_button(self.driver, locators['ConvertBtn'])

        # Scroll to end
        utils.scroll_to_multi_or_end(self.driver, 20)
