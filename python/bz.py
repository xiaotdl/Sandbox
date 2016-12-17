import os
import re
import time
import json
import random
import getpass
import requests

# scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]
BUGZ_HOST = 'bugzilla.olympus.f5net.com'
BUGZ_USER=os.environ["BUGZ_USER"] if "BUGZ_USER" in os.environ \
        else raw_input("Please enter your bugzilla username:")
BUGZ_PASSWORD=os.environ["BUGZ_PASSWORD"] if "BUGZ_PASSWORD" in os.environ \
        else getpass.getpass("Please enter your bugzilla password:")

user_agents=[
    'Python/Bugzilla',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'
]
USER_AGENT=random.choice(user_agents)


def _dumps(obj):
    return json.dumps(obj, indent=4, sort_keys=True)

def _print_request(r):
    url = r.request.url
    if 'Bugzilla_password' in url:
        url = re.sub("Bugzilla_password=.*", "Bugzilla_password=xxxxxx", url)
    print "==", time.strftime("%c"), "=="
    print r.request.method, url

def _save_response(response, path):
    with open(path, 'w') as f:
        f.write(str(response.status_code))
        f.write("</br>")
        f.write("<pre>" + _dumps(dict(response.headers)) + "</pre>")
        f.write("</br>")
        f.write(response.content)
    print "[%s] Response has been saved into file: %s.\n" % (response.status_code, path)


class Bugzilla(object):
    '''bzapi class.'''

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

        self.cookies = None
        self._login()

    def _do_request(self, url, print_request=True, response_file=None, **kwargs):
        r = requests.get(url,
                headers={'User-Agent': USER_AGENT},
                # verify=False, # enable in case SSLError
                **kwargs)
        if print_request:
            _print_request(r)
        if response_file:
            _save_response(r, response_file)
        return r

    def _login(self):
        url = 'https://{host}/{path}'.format(host=self.host, path='index.cgi')
        params = {
            'Bugzilla_login': self.user,
            'Bugzilla_password': self.password,
            'GoAheadAndLogIn': 'Log in',
        }
        r = self._do_request(url, params=params, response_file='index.html')
        self.cookies = r.cookies

    def query(self, params):
        url = 'https://{host}/{path}'.format(host=self.host, path='buglist.cgi')
        r = self._do_request(url, params=params, cookies=self.cookies, response_file='query.html')
        return r


if __name__ == '__main__':
    bz = Bugzilla(BUGZ_HOST, BUGZ_USER, BUGZ_PASSWORD)
    params = {
        'level1manager': 'gavrilov',
        'emailassigned_to1': 1,
        'email1': "xiaotian.li@f5.com",
        'bug_status': 'New',
        'product': 'FIT',
    }
    bz.query(params)


    print '== EOP =='


# >>>
# == Fri Dec 16 16:46:50 2016 ==
# GET https://bugzilla.olympus.f5net.com/index.cgi?GoAheadAndLogIn=Log+in&Bugzilla_login=xiaotian.li%40f5.com&Bugzilla_password=xxxxxx
# [200] Response has been saved into file: index.html.

# == Fri Dec 16 16:46:51 2016 ==
# GET https://bugzilla.olympus.f5net.com/buglist.cgi?level1manager=gavrilov&product=FIT&emailassigned_to1=1&bug_status=New&email1=xiaotian.li%40f5.com&list_id=6926091
# [200] Response has been saved into file: query.html.

# == EOP ==
