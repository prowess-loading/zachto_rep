from pages.loan_calculator import LoanCalculator
from pages.boat_loan_calculator import BoatLoanCalculator
from pages.loan_payoff_calculator import LoanPayoffCalculator
from pages.car_loan_calculator import CarLoanCalculator
from pages.compound_interest_calculator import CompoundInterestCalculator
from pages.forex_compounding_calculator import ForexCompoundingCalculator
from pages.cagr_calculator import CAGRCalculator
from pages.amortization_calculator import AmortizationCalculator
from pages.currency_converter import CurrencyConverter
from pages.million_to_billion_converter import MillionToBillionConverter
from pages.irr_calculator import IRRCalculator
from pages.margin_calculator import MarginCalculator
from pages.sip_calculator import SIPCalculator
from pages.simple_interest_calculator import SimpleInterestCalculator
from pages.price_per_sqft_calculator import PricePerSquareFeetCalculator
from pages.hourly_salary_calculator import HourlySalaryCalculator
from pages.savings_calculator import SavingsCalculator
from pages.mortgage_calculator import MortgageCalculator
from pages.apy_calculator import APYCalculator
from pages.credit_card_calculator import CreditCardCalculator
from pages.salary_to_hourly_calculator import SalaryToHourlyCalculator


class CalculatorFactory:
    @staticmethod
    def invoke_calculator(driver, calculator_name):
        # Mapping of calculator names to classes
        calculators = {
            "LoanCalculator": LoanCalculator,
            "BoatLoanCalculator": BoatLoanCalculator,
            "LoanPayoffCalculator": LoanPayoffCalculator,
            "CarLoanCalculator": CarLoanCalculator,
            "CompoundInterestCalculator": CompoundInterestCalculator,
            "ForexCompoundingCalculator": ForexCompoundingCalculator,
            "CAGRCalculator": CAGRCalculator,
            "AmortizationCalculator": AmortizationCalculator,
            "CurrencyConverter": CurrencyConverter,
            "MillionToBillionConverter": MillionToBillionConverter,
            "IRRCalculator": IRRCalculator,
            "MarginCalculator": MarginCalculator,
            "SIPCalculator": SIPCalculator,
            "SimpleInterestCalculator": SimpleInterestCalculator,
            "PricePerSquareFeetCalculator": PricePerSquareFeetCalculator,
            "HourlySalaryCalculator": HourlySalaryCalculator,
            "SavingsCalculator": SavingsCalculator,
            "MortgageCalculator": MortgageCalculator,
            "APYCalculator": APYCalculator,
            "CreditCardCalculator": CreditCardCalculator,
            "SalaryToHourlyCalculator": SalaryToHourlyCalculator,
        }

        # Mapping of calculator names to operation functions
        operation_methods = {
            "LoanCalculator": "loan_calculator_operations",
            "BoatLoanCalculator": "boat_loan_calculator_operations",
            "LoanPayoffCalculator": "loan_payoff_calculator_operations",
            "CarLoanCalculator": "car_loan_calculator_operations",
            "CompoundInterestCalculator": "compound_interest_calculator_operations",
            "ForexCompoundingCalculator": "forex_compounding_calculator_operations",
            "CAGRCalculator": "cagr_calculator_operations",
            "AmortizationCalculator": "amortization_calculator_operations",
            "CurrencyConverter": "currency_converter_operations",
            "MillionToBillionConverter": "million_to_billion_converter_operations",
            "IRRCalculator": "irr_calculator_operations",
            "MarginCalculator": "margin_calculator_operations",
            "SIPCalculator": "sip_calculator_operations",
            "SimpleInterestCalculator": "simple_interest_calculator_operations",
            "PricePerSquareFeetCalculator": "price_per_sqft_calculator_operations",
            "HourlySalaryCalculator": "hourly_salary_calculator_operations",
            "SavingsCalculator": "savings_calculator_operations",
            "MortgageCalculator": "mortgage_calculator_operations",
            "APYCalculator": "apy_calculator_operations",
            "CreditCardCalculator": "credit_card_calculator_operations",
            "SalaryToHourlyCalculator": "salary_to_hourly_calculator_operations",
        }

        calculator_class = calculators.get(calculator_name)
        # calculator_class = LoanCalculator
        operation_method_name = operation_methods.get(calculator_name)

        if not calculator_class or not operation_method_name:
            raise ValueError(
                f"Calculator '{calculator_name}' or its operation method is not defined in the factory."
            )

        # Instantiate the calculator class
        calculator_instance = calculator_class(driver)

        # Call the operation method dynamically
        if hasattr(calculator_instance, operation_method_name):
            getattr(calculator_instance, operation_method_name)()
        else:
            raise AttributeError(
                f"The calculator class '{calculator_name}' does not have the method '{operation_method_name}'."
            )
