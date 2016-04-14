#!/usr/bin/python
import re
import sys

class Problem:
    def __init__(self):
        self.id = -1
        self.title = ''
        self.tags = []
        self.ac_rate = ''
        self.difficulty = ''

    def parse_complete(self):
        return (self.id != -1 and self.title and self.tags and self.ac_rate and self.difficulty)

    def __str__(self):
        delimiter = ', '
        return (self.id + delimiter +
                self.title + delimiter +
                delimiter.join(self.tags) + delimiter +
                self.ac_rate + delimiter +
                self.difficulty)


def parse(line, problem):
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
    if m and problem.id == -1:
        problem.id = m.group(1).replace(',', '');
        return

    m = re.match(r""".*"title" : "<a href='/problems/[a-z0-9-]+/'>([^<]+)</a>.*""", line)
    if m and not problem.title:
        problem.title = m.group(1).replace(',', '');

    m = re.match(r""".*"<a class='btn btn-xs btn-default' href='/tag/[a-z0-9-]+/'>([^<]+)</a> "+.*""", line)
    if m:
        problem.tags.append(m.group(1).replace(',', ''));

    m = re.match(r""".*"ac_rate" : "([0-9.]+%)".*""", line)
    if m and not problem.ac_rate:
        problem.ac_rate = m.group(1).replace(',', '');

    m = re.match(r""".*"difficulty" : "<span value=\d+>([^<]+)</span>".*""", line)
    if m and not problem.difficulty:
        problem.difficulty = m.group(1).replace(',', '');

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print './parse.py <html_file>'
        sys.exit(1)

    FILENAME = sys.argv[1]

    problem = None
    problems = []

    with open(FILENAME, 'r') as f:
        for line in f.readlines():
            if not problem:
                problem = Problem()
            parse(line, problem)
            if problem.parse_complete():
                problems.append(problem)
                print str(problem)
                problem = None
