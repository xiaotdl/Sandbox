"""
reference: https://2.python-requests.org//en/master/

an example to use python requests library to:
  1. send a http request
  2. receives a http response and do some work with it

To execute:
$ python3.6 test.py
"""

import requests


URL = "https://jsonplaceholder.typicode.com/todos/1"
# >>>
# {
#   "userId": 1,
#   "id": 1,
#   "title": "delectus aut autem",
#   "completed": false
# }
#

resp = requests.get(URL)
print(resp.status_code)

print(resp.headers)
# >>> 'Content-Type': 'application/json; charset=utf-8'

print(resp.text) # raw http body

json_resp = resp.json() # serialize raw http body into json format
print(json_resp["userId"])
print(json_resp["id"])
print(json_resp["title"])
print(json_resp["completed"])

