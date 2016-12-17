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

def parse_bug_number(html):
    reg = re.compile("\<span class=\"bz_result_count\"\>(?P<num>\d+) bugs found.\s+\<\/span\>")
    sea = reg.search(html)
    return html[sea.start('num'):sea.end('num')]

def parse_bug_infomation(html):
    reg = re.compile("(?P<bug>\<tr\sid=\"b\d+\"\sclass=\"bz_bugitem.*?\<\/tr\>)", re.DOTALL)
    seaall = reg.findall(html)
    all_bug_details = []
    for i in range(len(seaall)):
        all_bug_details.append(parse_bug_detail(seaall[i]))
    return all_bug_details
    #print seaall[5]
    #print all_bug_details[5]

def print_bug_details(bug_details):
    for i in [1,2,3,4,9]:
        column_count = count_list([j[i] for j in bug_details])
        for key in column_count.keys():
            print key, ",", column_count[key]


        print " "
        print " "

def parse_time_info(bug_details):
    opened_list = list(i[8] for i in bug_details)
    opened_list.sort()
    fixed_list = list(i[6] for i in bug_details)
    fixed_list = [i.split(' ')[0] for i in fixed_list if i != ""]
    fixed_list = [i for i in fixed_list if i is not None]
    fixed_list.sort()
    start_year1 = int(opened_list[0].split('-')[0])
    start_month1 = int(opened_list[0].split('-')[1])
    start_year2 = int(fixed_list[0].split('-')[0])
    start_month2 = int(fixed_list[0].split('-')[1])
    if start_year1 < start_year2:
        start_year = start_year1
        start_month = start_month1
    elif start_year2 < start_year1:
        start_year = start_year2
        start_month = start_month2
    else:
        start_year = start_year1
        if start_month1 < start_month2:
            start_month = start_month1
        else:
            start_month = start_month2
    end_year1 = int(opened_list[-1].split('-')[0])
    end_month1 = int(opened_list[-1].split('-')[1])
    end_year2 = int(fixed_list[-1].split('-')[0])
    end_month2 = int(fixed_list[-1].split('-')[1])
    if end_year1 > end_year2:
        end_year = end_year1
        end_month = end_month1
    elif end_year2 > end_year1:
        end_year = end_year2
        end_month = end_month2
    else:
        end_year = end_year1
        if end_month1 > end_month2:
            end_month = end_month1
        else:
            end_month = end_month2
    time_info = {}
    year = start_year
    month = start_month
    while year != end_year or month != end_month + 1:
        if month == 13:
            year += 1
            month = 1
        time_info[str(year)+'-'+"%02d" % month] = [0,0]
        month += 1
    for i in range(len(opened_list)):
        opened_year = opened_list[i].split('-')[0]
        opened_month = opened_list[i].split('-')[1]
        time_info[opened_year+'-'+opened_month][0] += 1
        if i < len(fixed_list):
            fixed_year = fixed_list[i].split('-')[0]
            fixed_month = fixed_list[i].split('-')[1]
            time_info[fixed_year+'-'+fixed_month][1] += 1
    year = start_year
    month = start_month
    lastmonth_opened = 0
    lastmonth_fixed = 0
    while year != end_year or month != end_month + 1:
        if month == 13:
            year += 1
            month = 1
        time_info[str(year)+'-'+"%02d" % month].append(time_info[str(year)+'-'+"%02d" % month][0] + lastmonth_opened)
        time_info[str(year)+'-'+"%02d" % month].append(time_info[str(year)+'-'+"%02d" % month][1] + lastmonth_fixed)
        time_info[str(year)+'-'+"%02d" % month].append(time_info[str(year)+'-'+"%02d" % month][2]-time_info[str(year)+'-'+"%02d" % month][3])
        lastmonth_opened = time_info[str(year)+'-'+"%02d" % month][2]
        lastmonth_fixed = time_info[str(year)+'-'+"%02d" % month][3]
        month += 1
    return time_info

def print_time_info(time_info):
    time_span = list(time_info.keys())
    time_span.sort()
    for i in range(len(time_span)):
        string = time_span[i] +","
        for j in range(5):
            string += str(time_info[time_span[i]][j])
            string += ","
        print string[:-1]

def count_list(buglist):
    result = {}
    for i in range(len(buglist)):
        if buglist[i] in result:
            result[buglist[i]] += 1
        else:
            result[buglist[i]] = 1
    return result


def count_team(manager, bug_details):
    column_count = count_list([j[7] for j in bug_details])
    for key in column_count.keys():
        if key in team_name:
            column_count[key] += int(manager[key])
    column_count["asami"] = column_count["jgoodwin"]
    del column_count["jgoodwin"]
    for key in column_count.keys():
        print key, ",", column_count[key]
    print " "
    print " "


def parse_bug_detail(bughtml):
    reg_id = "\<a href=\"show_bug\.cgi\?id=\d+(\-\d)?\"\>(?P<id>\d+(\-\d)?)\</a\>"
    reg_column = "class=\"bz_component_column\"\>\s+\<span\stitle=\"(?P<component>.*?)\"\>"
    reg_column += ".*?class=\"bz_assigned_to_realname_column\"\>\s+\<span\stitle=\"(?P<assignee>.*?)\"\>"
    reg_column += ".*?class=\"bz_bug_status_column\"\>\s+\<span\stitle=\"(?P<status>.*?)\"\>"
    reg_column += ".*?class=\"bz_resolution_column\"\>\s+\<span\stitle=\"(?P<resolution>.*?)\"\>"
    reg_column += ".*?class=\"bz_cf_assigneddate_column\"\>(?P<assigneddate>.*?)\s+\</td\>"
    reg_column += ".*?class=\"bz_cf_fixeddate_column\"\>(?P<fixdate>.*?)\s+\</td\>"
    reg_column += ".*?class=\"bz_level1manager_column\"\>(?P<manager>.*?)\s+\</td\>"
    reg_column += ".*?class=\"bz_opendate_column\"\>(?P<opendate>.*?)\s+\</td\>"
    reg_column += ".*?class=\"bz_cf_type_column\"\>(?P<type>.*?)\s+\</td\>"
    reg = re.compile(reg_id + ".*?" + reg_column, re.DOTALL)
    bug_info = reg.search(bughtml)
    bug_detail = []
    bug_detail.append(bughtml[bug_info.start('id'):bug_info.end('id')])
    bug_detail.append(bughtml[bug_info.start('component'):bug_info.end('component')])
    bug_detail.append(bughtml[bug_info.start('assignee'):bug_info.end('assignee')])
    bug_detail.append(bughtml[bug_info.start('status'):bug_info.end('status')])
    bug_detail.append(bughtml[bug_info.start('resolution'):bug_info.end('resolution')])
    bug_detail.append(bughtml[bug_info.start('assigneddate'):bug_info.end('assigneddate')])
    bug_detail.append(bughtml[bug_info.start('fixdate'):bug_info.end('fixdate')])
    bug_detail.append(bughtml[bug_info.start('manager'):bug_info.end('manager')])
    bug_detail.append(bughtml[bug_info.start('opendate'):bug_info.end('opendate')])
    bug_detail.append(bughtml[bug_info.start('type'):bug_info.end('type')])
    return bug_detail


class Bugzilla(object):
    '''bzapi class.'''

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

        self.cookies = None

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

    def login(self):
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
    bz.login()
    params = {
        'level1manager': 'gavrilov',
        # 'emailassigned_to1': 1,
        # 'email1': "xiaotian.li@f5.com",
        # 'bug_status': 'New',
        'product': 'FIT',
        'columnlist': 'alias,component,assigned_to_realname,bug_status,resolution,cf_assigneddate,cf_fixeddate,level1manager,opendate,cf_type'
    }
    bz.query(params)
    with open('query.html', 'r') as f:
        html = f.read()
        print parse_bug_number(html)

        bug_details = parse_bug_infomation(html)

        print_bug_details(bug_details)

        # team_bug_number = count_team(manager_bug_number, bug_details)

        time_info = parse_time_info(bug_details)


        print "open,fixed,overall opened,overall fixed,bug left"
        print_time_info(time_info)



    print '== EOP =='


# >>>
== Fri Dec 16 17:12:15 2016 ==
GET https://bugzilla.olympus.f5net.com/index.cgi?GoAheadAndLogIn=Log+in&Bugzilla_login=xiaotian.li%40f5.com&Bugzilla_password=xxxxxx
[200] Response has been saved into file: index.html.

== Fri Dec 16 17:12:22 2016 ==
GET https://bugzilla.olympus.f5net.com/buglist.cgi?columnlist=alias%2Ccomponent%2Cassigned_to_realname%2Cbug_status%2Cresolution%2Ccf_assigneddate%2Ccf_fixeddate%2Clevel1manager%2Copendate%2Ccf_type&level1manager=gavrilov&product=FIT&list_id=6926151
[200] Response has been saved into file: query.html.

1340
AFM , 107
BaDOS , 18
DOS-Tests , 4
BaDOS-Tests , 1
Bvt , 154
Web Editor , 12
AVR-Tests , 5
Tests , 20
AVR , 56
General , 163
PEM , 373
FPS-Test , 2
AFM-Tests , 6
Replay Tool , 2
FPS , 79
DOS , 35
TCE , 23
ASM-Tests , 1
ASM , 278
PSM , 1


Sandar Lu , 38
Niv Bronstein , 188
Erez Arbell , 29
Aviv Katz , 130
Raja Kottapalli , 456
Xiaotian Li , 41
Illia Bobyr , 406
Evgeny Kagan - T , 52


Resolved , 274
Verified , 521
Reopened , 14
Closed , 52
Not Verified , 73
Test , 36
New , 358
Accepted , 12


NOT REPRODUCIBLE , 15
INVALID , 37
--- , 384
ENVIRONMENTAL , 2
DUPLICATE , 46
NOT DIAGNOSABLE , 1
FUNCTIONS AS DESIGNED , 26
WONTFIX , 32
FIXED , 797


Requirement , 63
Vulnerability , 1
Documentation , 8
Defect , 1015
Testability , 1
Improvement , 226
Action Item , 4
Test Case , 1
Performance , 2
Issue , 1
Regression , 15
Usability , 3


open,fixed,overall opened,overall fixed,bug left
2010-10,1,0,1,0,1
2010-11,0,0,1,0,1
2010-12,0,0,1,0,1
2011-01,1,0,2,0,2
2011-02,0,0,2,0,2
2011-03,0,0,2,0,2
2011-04,0,0,2,0,2
2011-05,1,0,3,0,3
2011-06,0,0,3,0,3
2011-07,1,0,4,0,4
2011-08,0,0,4,0,4
2011-09,0,0,4,0,4
2011-10,0,0,4,0,4
2011-11,0,0,4,0,4
2011-12,0,0,4,0,4
2012-01,0,0,4,0,4
2012-02,0,0,4,0,4
2012-03,2,0,6,0,6
2012-04,4,0,10,0,10
2012-05,0,0,10,0,10
2012-06,1,0,11,0,11
2012-07,0,0,11,0,11
2012-08,3,0,14,0,14
2012-09,3,0,17,0,17
2012-10,6,3,23,3,20
2012-11,11,6,34,9,25
2012-12,5,2,39,11,28
2013-01,3,1,42,12,30
2013-02,10,7,52,19,33
2013-03,7,0,59,19,40
2013-04,37,32,96,51,45
2013-05,10,2,106,53,53
2013-06,19,5,125,58,67
2013-07,18,8,143,66,77
2013-08,31,29,174,95,79
2013-09,17,13,191,108,83
2013-10,28,25,219,133,86
2013-11,7,12,226,145,81
2013-12,14,15,240,160,80
2014-01,31,10,271,170,101
2014-02,25,18,296,188,108
2014-03,31,43,327,231,96
2014-04,32,24,359,255,104
2014-05,25,32,384,287,97
2014-06,33,24,417,311,106
2014-07,28,19,445,330,115
2014-08,56,46,501,376,125
2014-09,30,17,531,393,138
2014-10,20,21,551,414,137
2014-11,15,12,566,426,140
2014-12,24,11,590,437,153
2015-01,32,25,622,462,160
2015-02,46,38,668,500,168
2015-03,43,31,711,531,180
2015-04,22,17,733,548,185
2015-05,29,32,762,580,182
2015-06,23,16,785,596,189
2015-07,20,10,805,606,199
2015-08,11,3,816,609,207
2015-09,4,3,820,612,208
2015-10,12,6,832,618,214
2015-11,15,9,847,627,220
2015-12,22,12,869,639,230
2016-01,27,13,896,652,244
2016-02,25,8,921,660,261
2016-03,46,17,967,677,290
2016-04,27,16,994,693,301
2016-05,21,7,1015,700,315
2016-06,28,15,1043,715,328
2016-07,40,22,1083,737,346
2016-08,61,44,1144,781,363
2016-09,43,30,1187,811,376
2016-10,67,52,1254,863,391
2016-11,57,59,1311,922,389
2016-12,29,34,1340,956,384
== EOP ==
