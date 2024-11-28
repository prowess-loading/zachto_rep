import json
import random
from setup.smooth_scroll import SmoothScroll


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Load locators from the JSON file
        with open('data/page_locators.json', 'r') as f:
            self.locators = json.load(f)

        # List of calculators
        self.calculators = [
            "LoanCalculator",
            "BoatLoanCalculator",
            "LoanPayoffCalculator",
            "CompoundInterestCalculator",
            "ForexCompoundingCalculator",
            "CAGRCalculator",
            "AmortizationCalculator",
            "CurrencyConverter",
            "MillionToBillionConverter",
            "IRRCalculator",
            "MarginCalculator",
            "SIPCalculator",
            "SimpleInterestCalculator",
            "HourlySalaryCalculator",
            "CarLoanCalculator",              # Not available in the Home page currently
            "PricePerSquareFeetCalculator",   # Not available in the Home page currently
            "SavingsCalculator",              # Not available in the Home page currently
            "MortgageCalculator",             # Not available in the Home page currently
            "APYCalculator",                  # Not available in the Home page currently
            "CreditCardCalculator",           # Not available in the Home page currently
            "SalaryToHourlyCalculator"        # Not available in the Home page currently
        ]

        self.selected_calculator = random.choice(self.calculators)
        # self.selected_calculator = "LoanCalculator"

    def open_calculator(self):
        calculator_locator = self.locators["Calculators"].get(
            self.selected_calculator)
        print(f"Opening the {self.selected_calculator}...")

        if calculator_locator:
            navigator = SmoothScroll(self.driver, speed=20.0)
            navigator.navigate_and_scroll(calculator_locator)

        else:
            print(f"Locator not found for {self.selected_calculator}")
