import sys
import time
import logging
import requests
from celery.states import SUCCESS

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
LOG.addHandler(logging.StreamHandler(sys.stdout))


API_SERVER = "127.0.0.1:5000"
API_SERVER_URI = "http://%s" % API_SERVER


def curl(method, url, **kwargs):
    LOG.debug("curl -X {method} {url}".format(method=method, url=url))
    r = requests.request(method, url, **kwargs)
    LOG.debug(r.status_code)
    LOG.debug(r.text)
    return r


def wait_task(selflink, interval=1, timeout=60, timeout_msg="Timeout!", success_state=SUCCESS):
    end_time = time.time() + 60
    while True:
        if time.time() > end_time:
            raise Exception(timeout_msg)
        r = curl("GET", selflink)
        if r.json()["state"] == success_state:
            break
        time.sleep(interval)


def main():
    r = curl("POST", API_SERVER_URI + "/task")
    selflink = r.headers['Location']

    wait_task(selflink, timeout=60)

    return 0

if __name__ == '__main__':
    sys.exit(main())
