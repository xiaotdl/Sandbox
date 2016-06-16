import time
import requests
from bs4 import BeautifulSoup

from test_sendmail import sendmail

# visit website
response = requests.get('http://icert.doleta.gov/')

# parse info from response
soup = BeautifulSoup(response.content, "html.parser")
current_request_date = soup.find("div", {"id": "processingpost"}).find("table").find("tbody").find("tr").find("td").text
request_date_changed = current_request_date != u'March\xa02016'

# construct email and send it out
datetime = time.strftime("%c")
msg = (datetime + '\n'
       'http://icert.doleta.gov/\n')
if request_date_changed:
    msg += 'request date has changed to: %s!!!' % current_request_date
else:
    msg += 'request date is not changed: %s.' % current_request_date
sendmail('xiaotdl@gmail.com', 'prevailing wage determination', msg.encode('ascii', 'ignore'))
