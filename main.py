from setup.browser_setup import BrowserSetup
import json
from pages.homepage import HomePage
import time
from setup.calculator_factory import CalculatorFactory


def main():
    with open('data/urls.json', 'r') as f:
        urls = json.load(f)

    try:
        num_tests = int(
            input("How many times do you want to run the test? (Max: 1000)"))
        if num_tests <= 0:
            print("The number of tests should be greater than 0.")
            return
        if num_tests > 1000:
            print("The maximum number of tests allowed is 1000.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(1, num_tests + 1):
        start_time = time.time()
        print(f"\nRunning test #{i}...\n")
        driver = None

        try:
            #! Setup the browser
            browser_setup = BrowserSetup()
            driver = browser_setup.setup_browser(
                device_name="random",        # random
                browser_name="random",       # random, chrome, firefox, edge, safari
                region="usa"                 # usa, eu
            )

            driver.get(urls["MainPage"])
            homepage_run = HomePage(driver)
            homepage_run.open_calculator()

            selected_calculator = homepage_run.selected_calculator
            try:
                CalculatorFactory.invoke_calculator(
                    driver, selected_calculator)
            except Exception as e:
                print(f"An error occurred while running the calculator: {e}")

        finally:
            if driver:
                driver.quit()
            print(f"Test #{i} completed in {time.time() - start_time:.2f}s.")


if __name__ == "__main__":
    main()
