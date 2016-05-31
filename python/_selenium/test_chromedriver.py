# Ref:
# ChromeDriver - WebDriver for Chrome
# https://sites.google.com/a/chromium.org/chromedriver/getting-started
# Description:
#     ChromeDriver is a separate executable that Selenium.WebDriver uses to control Chrome.
# Prerequisites:
#     - Download chromdriver.exe from http://chromedriver.storage.googleapis.com/index.html
#     - Include the chromedriver.exe location in your PATH environment variable.

import time
from selenium import webdriver

driver = webdriver.Chrome("C:/cygwin/home/amw/chromedriver.exe") # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
raw_input('enter anything to quit...')
driver.quit()
