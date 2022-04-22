"""
This module contains web test cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



@pytest.fixture
def browser():
  # Initialize ChromeDriver
  driver = Chrome()
 
  # Wait implicitly for elements to be ready before attempting interactions
  driver.implicitly_wait(10)

  # Return the driver object at the end of setup
  yield driver
  
  # For cleanup, quit the driver
  driver.quit()


def test_booking_login_positive(browser):
  # Set up some test case data
  URL = 'https://www.booking.com/index.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaOkBiAEBmAEJuAEXyAEV2AED6AEBiAIBqAIDuALv_9WSBsACAdICJDMxNTdkMWU2LTM1NTctNGFjZC1iN2VkLTQxYmMwYWUyOTY2YdgCBOACAQ;sid=3bb430307a4c41197c721b787c782d50;keep_landing=1&sb_price_type=total&'
  PHRASE1 = 'anton.bandera2022@gmail.com'
  PHRASE2 = '12345678qQ'

  # Navigate to the Booking home page
  browser.get(URL)

  # Find the search link element
  continue_link = browser.find_element_by_link_text('Sign in')
  continue_link.click()
  sleep(2)

  # Find the search input element
  search_input = browser.find_element_by_xpath("//input[@id='username']")

  # Send a search phrase to the input and hit the RETURN key
  search_input.send_keys(PHRASE1 + Keys.RETURN)
  sleep(2)

  # Find the search input element
  search_input = browser.find_element_by_xpath("//input[@id='password']")

  # Send a search phrase to the input and hit the RETURN key
  search_input.send_keys(PHRASE2 + Keys.RETURN)
  sleep(2)

  # Human detection
  element = browser.find_element_by_css_selector('#px-captcha')
  action = ActionChains(browser)
  click = ActionChains(browser)
  action.click_and_hold(element)
  action.perform()
  sleep(2)

def test_booking_login_negative(browser):
  # Set up some test case data
  URL = 'https://www.booking.com/index.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaOkBiAEBmAEJuAEXyAEV2AED6AEBiAIBqAIDuALv_9WSBsACAdICJDMxNTdkMWU2LTM1NTctNGFjZC1iN2VkLTQxYmMwYWUyOTY2YdgCBOACAQ;sid=3bb430307a4c41197c721b787c782d50;keep_landing=1&sb_price_type=total&'
  PHRASE1 = 'anton.bandera202@gmail.com'
  PHRASE2 = '12345678qQ'

  # Navigate to the Booking home page
  browser.get(URL)

  # Find the search link element
  continue_link = browser.find_element_by_link_text('Sign in')
  continue_link.click()
  sleep(2)

  # Find the search input element
  search_input = browser.find_element_by_xpath("//input[@id='username']")

  # Send a search phrase to the input and hit the RETURN key
  search_input.send_keys(PHRASE1 + Keys.RETURN)
  sleep(2)

  # Find the search input element
  search_input = browser.find_element_by_xpath("//input[@id='password']")

  # Send a search phrase to the input and hit the RETURN key
  search_input.send_keys(PHRASE2 + Keys.RETURN)
  sleep(2)

  # Human detection
  element = browser.find_element_by_css_selector('#px-captcha')
  action = ActionChains(browser)
  click = ActionChains(browser)
  action.click_and_hold(element)
  action.perform()
  sleep(2)