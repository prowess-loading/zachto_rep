import sys
import time
from setup.browser_setup import BrowserSetup
from pages.homepage import HomePage
from setup.calculator_factory import CalculatorFactory
from setup import utils


def main():

    if len(sys.argv) > 1:
        try:
            num_tests = int(sys.argv[1])
            if num_tests <= 0:
                print("The number of tests should be greater than 0.")
                return
            if num_tests > 1000:
                print("The maximum number of tests allowed is 1000.")
                return
        except ValueError:
            print("Please provide a valid number for <num_tests>.")
            return
    else:
        try:
            num_tests = int(
                input("How many times do you want to run the test? (Max: 1000): "))
            if num_tests <= 0:
                print("The number of tests should be greater than 0.")
                return
            if num_tests > 1000:
                print("The maximum number of tests allowed is 1000.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

    device_type = "desk"        # desk, mobile
    proxy_active = True         # True, False

    # Execute tests
    for i in range(1, num_tests + 1):
        start_time = time.time()
        print(f"\nRunning test #{i}...\n")
        driver = None

        try:
            # Setup the browser
            browser_setup = BrowserSetup()
            driver = browser_setup.setup_browser(
                device_type,
                proxy_active,
                device_name="random",       # random
                browser_name="random",      # random, chrome, firefox, edge, safari
                region="us"                 # rd, us, na, au, as, eu
            )

            # Open main page and run calculator
            target_url = utils.target_url()
            driver.get(target_url)
            homepage_run = HomePage(driver)
            homepage_run.open_calculator()

            selected_calculator = homepage_run.selected_calculator
            try:
                elapsed_time = time.time() - start_time
                if elapsed_time > 180:
                    print(
                        f"Quitting current browser...")
                    driver.quit()
                    continue
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
