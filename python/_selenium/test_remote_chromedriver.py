# Ref:
# Using Selenium with remote WebDriver
# http://selenium-python.readthedocs.io/getting-started.html#using-selenium-with-remote-webdriver
# Prerequisites:
#     - Download selenium-server.jar from http://www.seleniumhq.org/download/
#     - Download chromedriver.exe from http://chromedriver.storage.googleapis.com/index.html
#     - run remote selenium-server.jar on remote server side box
#       $ ssh amw@10.192.10.149 java -jar /cygwin/home/amw/selenium.jar -Dwebdriver.chrome.driver='/cygwin/home/amw/chromedriver.exe'
#       15:43:06.471 INFO - Launching a standalone Selenium Server
#       ...
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
