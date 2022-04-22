"""
This module contains web test cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
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

def test_booking(browser):
  # Set up some test case data
  URL = 'https://www.booking.com/index.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaOkBiAEBmAEJuAEXyAEV2AED6AEBiAIBqAIDuALv_9WSBsACAdICJDMxNTdkMWU2LTM1NTctNGFjZC1iN2VkLTQxYmMwYWUyOTY2YdgCBOACAQ;sid=3bb430307a4c41197c721b787c782d50;keep_landing=1&sb_price_type=total&'
  PHRASE1 = 'anton.bandera22@gmail.com'
  PHRASE2 = '12345678qQ'

  # Navigate to the Booking home page
  browser.get(URL)

  PHRASE = 'travel'

  # Find the search link element
  continue_link = browser.find_element_by_link_text('Attractions')

  continue_link.click()

  # Find the search input element
  search_input = browser.find_element_by_xpath("//input[@data-testid='search-input-field']")
  
  # Send a search phrase to the input and hit the RETURN key
  search_input.send_keys(PHRASE + Keys.RETURN)

  sleep(2)

  # Find the search button element

  button = browser.find_element_by_xpath("//button[@type='submit']")

  assert button.text == 'Search'

  button.click()
  
  sleep(2)

  # Find the search label element

  label = browser.find_element_by_xpath("//label[input/@value='museums']")

  label.click()

  sleep(2)

  # Find the search div element

  div = browser.find_element_by_xpath("//div[@class='c90eaff0bf c3294bb3d3']/div[1]")

  div.click()

  sleep(2)

  # Find the search id element

  element = browser.find_element_by_xpath("//*[@id='attr-product-page-main-content']/div[5]/h2")

  assert element.text+(' London - Booking.com') == browser.title