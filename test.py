from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from setup import utils

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://sub01.zachto.xyz/finance/compound-interest-calculator.php")

locators = utils.load_locators("CompoundInterestCalculator")

# utils.scroll_to_calculate_button(driver)
utils.select_dropdown(driver, locators["compoundFreq"], '360')
sleep(15)
