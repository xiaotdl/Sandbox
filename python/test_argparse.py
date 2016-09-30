#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser(prog='test_argparse.py')

parser.add_argument('-v', '--var', dest='var')
parser.add_argument('--include-tests', dest='include_tests', nargs='+')
parser.add_argument('--include-daemons', dest='include_daemons', nargs='+')

args = parser.parse_args()

print args.var
print args.include_tests
print args.include_daemons

# >>>
# $ ./test_argparse.py -v abc --include-tests 44 55 66
# abc
# ['44', '55', '66']
