# Ref:
# Using Selenium with remote WebDriver
# http://selenium-python.readthedocs.io/getting-started.html#using-selenium-with-remote-webdriver
# Prerequisites:
#     - Download selenium-server.jar from http://www.seleniumhq.org/download/
#     - run selenium-server.jar on remote server side box
#       $ java -jar selenium-server-standalone-2.x.x.jar
#       15:43:07.541 INFO - RemoteWebDriver instances should connect to: http://127.0.0.1:4444/wd/hub
#       15:43:07.554 INFO - Selenium Server is up and running

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://10.192.10.149:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME
)
driver.get('http://www.google.com/');
search_box = driver.find_element_by_name('q')
search_box.send_keys("ChromeDriver")
search_box.submit()
raw_input('enter anything to quit...')
driver.quit()
