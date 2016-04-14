#!/usr/bin/python
import re
import sys


def parse(line):
    #
    # raw data looks like this:
    #
    # {
    #   "ac_or_not": "<span class='None'/>",
    #   "id" : "15",
    #   "title" : "<a href='/problems/3sum/'>3Sum</a> "+
    #       ""+
    #       "<div class='tags tag_margin'>"+
    #         ""+
    #           "<a class='btn btn-xs btn-default' href='/tag/array/'>Array</a> "+
    #         ""+
    #           "<a class='btn btn-xs btn-default' href='/tag/two-pointers/'>Two Pointers</a> "+
    #         ""+
    #       "</div>"+
    #       "",
    #   "ac_rate" : "18.7%",
    #   "difficulty" : "<span value=2>Medium</span>"
    # },
    m = re.match(r""".*"id" : "([0-9]+)".*""", line)
    if m:
        id = m.group(1); print id.replace(',', '')+',',

    m = re.match(r""".*"title" : "<a href='/problems/[a-z0-9-]+/'>([^<]+)</a>.*""", line)
    """"title" : "<a href='/problems/container-with-most-water/'>Container With Most Water</a>"""
    if m:
        title = m.group(1); print title.replace(',', '')+',',

    m = re.match(r""".*"<a class='btn btn-xs btn-default' href='/tag/[a-z0-9-]+/'>([^<]+)</a> "+.*""", line)
    if m:
        tag = m.group(1); print "'%s'" % tag.replace(',', ''),

    m = re.match(r""".*"ac_rate" : "([0-9.]+%)".*""", line)
    if m:
        ac_rate = m.group(1); print ', '+ac_rate.replace(',', '')+',',

    m = re.match(r""".*"difficulty" : "<span value=\d+>([^<]+)</span>".*""", line)
    if m:
        difficulty = m.group(1); print difficulty.replace(',', '')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print './parse.py <html_file>'
        sys.exit(1)

    FILENAME = sys.argv[1]

    with open(FILENAME, 'r') as f:
        for line in f.readlines():
            parse(line)
