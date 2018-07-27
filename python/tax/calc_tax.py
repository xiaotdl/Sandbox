#!/usr/bin/env python
"""
Python script to calculate tax for married couple filing jointly.

To compare with:
    https://smartasset.com/taxes/income-taxes
"""
import sys


DEBUG=False

def debug(msg):
    if DEBUG:
        print msg

# REF: Federal Income Tax
# https://taxfoundation.org/2018-tax-brackets/
STD_FEDERAL_COUPLE_DEDUCTION = 24000
FED_TAX_BRACKETS = [0, 19050, 77400, 165000, 315000, 400000, 600000, sys.maxint]
FED_TAX_RATES    = [0, 0.12,  0.22,  0.24,   0.32,   0.35,   0.37,   1]

# REF: CA State Income Tax
# https://taxfoundation.org/state-individual-income-tax-rates-brackets-2018/
STD_STATE_COUPLE_DEDUCTION = 8472
STATE_TAX_BRACKETS = [0,    16446, 38990, 61538, 85433, 107960, 551476, 661768, 1000000, 1074996, sys.maxint]
STATE_TAX_RATES    = [0.01, 0.02,  0.04,  0.06,  0.08,  0.093,  0.103,  0.113,  0.123,   0.133,   1]


def calc_tax(income, TAX_BRACKETS, TAX_RATES):
    tax = 0
    debug("== tax break down ==")
    debug("taxable_income, bracket_tax, effective_bracket_tax_rate")
    for i in range(len(TAX_BRACKETS) - 1):
        if income <= TAX_BRACKETS[i]:
            break
        taxable_income = min(income, TAX_BRACKETS[i + 1]) - TAX_BRACKETS[i]
        bracket_tax = int(taxable_income * TAX_RATES[i])
        debug("%s, %s, %.2f%%" % (taxable_income, bracket_tax, float(bracket_tax)/float(taxable_income) * 100))
        tax += bracket_tax
    return tax


def main():
    # == user input ==>
    income = 200000
    if len(sys.argv) >= 2:
        income = int(sys.argv[1])
    # <====

    # == federal tax ==>
    effective_federal_income = income - STD_FEDERAL_COUPLE_DEDUCTION
    federal_tax = calc_tax(effective_federal_income, FED_TAX_BRACKETS, FED_TAX_RATES)
    effective_federal_tax_rate = float(federal_tax) / float(effective_federal_income)
    # <====

    # == CA state tax ==>
    effective_state_income = income - federal_tax - STD_STATE_COUPLE_DEDUCTION
    state_tax = calc_tax(effective_state_income, STATE_TAX_BRACKETS, STATE_TAX_RATES)
    effective_state_tax_rate = float(state_tax) / float(effective_state_income)
    # <====

    # == total ==>
    total_tax = federal_tax + state_tax
    effective_total_tax_rate = float(total_tax) / float(income)
    # <====

    print "== federal tax =="
    print "effective_federal_income: %s" % effective_federal_income
    print "federal_tax: %s" % federal_tax
    print "effective_federal_tax_rate: %.2f%%" % (effective_federal_tax_rate * 100)

    print "== CA state tax =="
    print "effective_state_income: %s" % effective_state_income
    print "state_tax: %s" % state_tax
    print "effective_state_tax_rate: %.2f%%" % (effective_state_tax_rate * 100)

    print "== summary =="
    print "income: %s" % income
    print "total_tax: %s" % total_tax
    print "effective_total_tax_rate: %.2f%%" % (effective_total_tax_rate * 100)


if __name__ == '__main__':
    main()
