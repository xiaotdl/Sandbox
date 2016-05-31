"""
Ref:
stackoverflow: How to use Selenium with Python?
http://stackoverflow.com/questions/17540971/how-to-use-selenium-with-python
"""
import os

from selenium import webdriver

try:
    USERNAME = os.environ['USERNAME']
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    raise Exception("USERNAME and PASSWORD environment variable needs to be set:\n"
                    "$ export USERNAME=<your_username>\n"
                    "$ export PASSWORD=<your_password>\n")

XPATHS = {
    'usernameTxtBox' : "//input[@name='session_key']",
    'passwordTxtBox' : "//input[@name='session_password']",
    'submitButton' :   "//input[@name='submit']"
}

class LinkedinLoginDriver():
    driver = webdriver.Firefox()
    driver.get("http://www.linkedin.com/")
    driver.maximize_window()

    def login(self, username, password):
        #Clear Username TextBox if already allowed "Remember Me"
        self.driver.find_element_by_xpath(XPATHS['usernameTxtBox']).clear()
        #Write Username in Username TextBox
        self.driver.find_element_by_xpath(XPATHS['usernameTxtBox']).send_keys(username)

        #Clear Password TextBox if already allowed "Remember Me"
        self.driver.find_element_by_xpath(XPATHS['passwordTxtBox']).clear()
        #Write Password in password TextBox
        self.driver.find_element_by_xpath(XPATHS['passwordTxtBox']).send_keys(password)

        #Click Login button
        self.driver.find_element_by_xpath(XPATHS['submitButton']).click()

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    driver = LinkedinLoginDriver()
    driver.login(USERNAME, PASSWORD)
    raw_input("Click anything to quit...")
    driver.quit()
