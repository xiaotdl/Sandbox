#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser(prog='test_argparse.py')

parser.add_argument('-v', '--var', dest='var')
parser.add_argument('--include-tests', dest='include_tests', nargs='+')

args = parser.parse_args()

print args.var
print args.include_tests

# >>>
# $ ./test_argparse.py -v abc --include-tests 44 55 66
# abc
# ['44', '55', '66']
