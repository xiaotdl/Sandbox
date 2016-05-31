"""
# Ref:
# Selenium Tutorial: Web Scraping with Selenium and Python
# http://www.marinamele.com/selenium-tutorial-web-scraping-with-selenium-and-python

== Break Down ==
# INITIALIZE DRIVER
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.wait = WebDriverWait(driver, 5)


# WAIT FOR ELEMENTS
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

element = driver.wait.until(
    EC.presence_of_element_located(
    EC.element_to_be_clickable(
    EC.visibility_of_element_located(
        (By.NAME, "name")
        (By.ID, "id")
        (By.LINK_TEXT, "link text")
        (By.PARTIAL_LINK_TEXT, "partial link text")
        (By.TAG_NAME, "tag name")
        (By.CLASS_NAME, "class name")
        (By.CSS_SELECTOR, "css selector")
        (By.XPATH, "xpath")
    )
)


# CATCH EXCEPTIONS
from selenium.common.exceptions import (
    TimeoutException,
    ElementNotVisibleException
)
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementNotVisibleException,
)


class GoogleSearchDriver():
    driver = webdriver.Firefox()
    # make the driver wait a 5 seconds for an event to occur
    driver.wait = WebDriverWait(driver, 5)

    def lookup(self, query):
        self.driver.get("http://www.google.com")
        try:
            search_box = self.driver.wait.until(EC.presence_of_element_located(
                (By.NAME, "q")))
            button = self.driver.wait.until(EC.element_to_be_clickable(
                (By.NAME, "btnK")))
            search_box.send_keys(query)
            try:
                button.click()
            except ElementNotVisibleException:
                button = self.driver.wait.until(EC.visibility_of_element_located(
                    (By.NAME, "btnG")))
                button.click()
        except TimeoutException:
            print("SearchBox or Button not found in google.com!")

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    driver = GoogleSearchDriver()
    driver.lookup("Selenium")
    raw_input("Click anything to quit...")
    driver.quit()
