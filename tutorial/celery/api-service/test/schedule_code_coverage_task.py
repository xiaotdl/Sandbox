import sys
import time
import datetime
import logging
import requests

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
LOG.addHandler(logging.StreamHandler(sys.stdout))


# API_SERVER = "10.192.10.198:5000" # TESTING
API_SERVER = "10.192.10.198"
API_SERVER_URI = "http://%s" % API_SERVER

BIGIP_MGMT_IP = '10.192.10.243'


def do_task(bigip_mgmt_ip, mode):
    payload = {
        'name': 'test-code-coverage-task',
        'user': 'test',
        'priority': 10,
        'data': {
            'bigip-mgmt-ip': bigip_mgmt_ip,
            'module': 'afm',
            'daemons': 'autodosd',
            'mode': mode
        }
    }
    task_link = API_SERVER_URI + "/api/task/code-coverage"
    r = requests.post(task_link, json=payload)
    LOG.debug(str(datetime.datetime.now()))
    LOG.debug("curl -X POST {url} {body}".format(url=task_link, body=payload))
    LOG.debug(r.status_code)
    LOG.debug(r.text)
    if r.status_code/100 != 2:
        return (False, None)
    resultlink = r.headers['Location']
    return (True, resultlink)


def wait_task(selflink, interval=1, timeout=60, timeout_msg="Timeout!"):
    end_time = time.time() + timeout
    while True:
        if time.time() > end_time:
            raise Exception(timeout_msg)
        r = requests.get(selflink)
        LOG.debug(str(datetime.datetime.now()))
        LOG.debug("curl {url}".format(url=selflink))
        LOG.debug(r.status_code)
        LOG.debug(r.text)
        if r.status_code/100 != 2:
            return (False,)

        if r.json()["state"] == 'SUCCESS':
            return (True,)
        if r.json()["state"] == 'FAILURE':
            return (False,)

        time.sleep(interval)


def main():
    print sys.argv
    bigip_mgmt_ip = BIGIP_MGMT_IP
    if len(sys.argv) >= 2:
        bigip_mgmt_ip = sys.argv[1]

    mode = 'check'
    if len(sys.argv) >= 3:
        mode = sys.argv[2]

    (success, resultlink) = do_task(bigip_mgmt_ip, mode)
    if not success:
        return 1

    (success, ) = wait_task(resultlink, timeout=600)
    if not success:
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
