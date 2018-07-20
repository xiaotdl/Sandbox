#!/usr/bin/env python
"""
This script is running numbers and calculate cash flow stats.

REF: https://www.biggerpockets.com/renewsblog/2010/06/30/introduction-to-real-estate-analysis-investing/

TODO:
    - tax benefits(property tax/interest deductible, property depreciation)
    - loan paydown, property equity growth
    - property appreciation
    - projection of rent growth
"""
import sys


if len(sys.argv) >= 2:
    data_file = sys.argv[1]
    data_module = data_file.rstrip(".py").replace("/", ".")
    print "importing %s" % data_module
    exec("from %s import *" % data_module)
else:    
    from property_data.example import *
    print "Usage:"
    print "    python %s property_data/example.py" % sys.argv[0]
    print



MONS_PER_YR = 12


def calculate_mortgage_monthly_payment(loan, years, apr):
    """ref: https://www.mtgprofessor.com/formulas.htm"""
    c = apr/MONS_PER_YR
    n = MONS_PER_YR * years
    return loan * (c * (1 + c)**n) / ((1 + c)**n - 1)


# == invest/out-of-pocket ==
PURCHASE_PRICE = purchase_price

DOWNPAY_PERCENT = downpay_percent
DOWNPAY = PURCHASE_PRICE * DOWNPAY_PERCENT

CLOSING_COST = est_closing_cost

ACTUAL_PURCASE_PRICE = DOWNPAY + CLOSING_COST


# == financing/out-of-pocket ==
MORTGAGE_LOAN = PURCHASE_PRICE - DOWNPAY
MORTGAGE_LOAN_YRS = mortgage_loan_yrs
MORTGAGE_LOAN_APR = est_mortgage_loan_apr
MONTHLY_MORTGAGE_LOAN_PAYMENT = \
    calculate_mortgage_monthly_payment(MORTGAGE_LOAN, MORTGAGE_LOAN_YRS, MORTGAGE_LOAN_APR)
ANNUAL_MORTGAGE_PAYMENT = MONTHLY_MORTGAGE_LOAN_PAYMENT * MONS_PER_YR


# == tax/out-of-pocket ==
PROPERTY_TAX_RATE = property_tax_rate
ANNUAL_PROPERTY_TAX = PURCHASE_PRICE * PROPERTY_TAX_RATE


# == expense/out-of-pocket ==
MONTHLY_HOA_EXPENSE = est_monthly_hoa_expense
ANNUAL_HOA_EXPENSE = MONTHLY_HOA_EXPENSE * MONS_PER_YR

ANNUAL_HOME_INSURANCE_EXPENSE = est_annual_home_insurance_expense

ANNUAL_REPAIR_RESERVE_EXPENSE = est_annual_repair_reserve_expense

ANNUAL_MISC_EXPENSE = \
    ANNUAL_HOA_EXPENSE + \
    ANNUAL_HOME_INSURANCE_EXPENSE + \
    ANNUAL_REPAIR_RESERVE_EXPENSE


# == income/into-pocket ==
VACANCY_PERCENT = est_vacancy_percent

MONTHLY_RENT = est_monthly_rent
MONTHLY_EFFECTIVE_RENT =  MONTHLY_RENT * (1 - VACANCY_PERCENT)

ANNUAL_GROSS_INCOME = MONTHLY_EFFECTIVE_RENT * MONS_PER_YR


# == service/out-of-pocket ==
ANNUAL_PROPERTY_MANAGER_SERVICE_FEE_RATE = est_annual_property_manager_service_fee_rate
ANNUAL_PROPERTY_MANAGER_SERVICE_FEE = ANNUAL_PROPERTY_MANAGER_SERVICE_FEE_RATE * ANNUAL_GROSS_INCOME

ANNUAL_LAWN_SERVICE_FEE = est_annual_lawn_service_fee

ANNUAL_SERVICE_FEE = \
    ANNUAL_PROPERTY_MANAGER_SERVICE_FEE + \
    ANNUAL_LAWN_SERVICE_FEE

# == total/out-of-pocket ==
ANNUAL_TOTAL_EXPENSE = \
    ANNUAL_MORTGAGE_PAYMENT + \
    ANNUAL_PROPERTY_TAX + \
    ANNUAL_SERVICE_FEE + \
    ANNUAL_MISC_EXPENSE
MONTHLY_TOTAL_EXPENSE = ANNUAL_TOTAL_EXPENSE / MONS_PER_YR


# == cash flow/into-pocket ==
ANNUAL_NET_INCOME = ANNUAL_GROSS_INCOME - ANNUAL_TOTAL_EXPENSE
MONTHLY_NET_INCOME = ANNUAL_NET_INCOME / MONS_PER_YR


# == metric ==
# Capitalization Rate: return on income to property price
CAP_RATE = ANNUAL_NET_INCOME / PURCHASE_PRICE * 100

# Cash-on-Cash Return: return on income to actual money put in
CASH_ON_CASH_RETURN = ANNUAL_NET_INCOME / ACTUAL_PURCASE_PRICE * 100


def main():
    print "== addr == %s" % address
    print "== link == %s" % link
    print "== desp == %s" % description
    print

    print "== analysis =="
    print "HOUSE_VALUE: $%d" % PURCHASE_PRICE

    # out-of-pocket
    print "OUT_OF_POCKET: $%d" % ACTUAL_PURCASE_PRICE

    # balance sheet
    print "MONTHLY_TOTAL_EXPENSE: -$%d" % MONTHLY_TOTAL_EXPENSE
    print "\t%5.2f%%, %5d - MORTGAGE_PAYMENT" % (ANNUAL_MORTGAGE_PAYMENT / ANNUAL_TOTAL_EXPENSE * 100, ANNUAL_MORTGAGE_PAYMENT/MONS_PER_YR)
    print "\t%5.2f%%, %5d - PROPERTY_TAX" % (ANNUAL_PROPERTY_TAX / ANNUAL_TOTAL_EXPENSE * 100, ANNUAL_PROPERTY_TAX/MONS_PER_YR)
    print "\t%5.2f%%, %5d - SERVICE_FEE(PROPERTY_MGMT,LAWN)" % (ANNUAL_SERVICE_FEE / ANNUAL_TOTAL_EXPENSE * 100, ANNUAL_SERVICE_FEE/MONS_PER_YR)
    print "\t%5.2f%%, %5d - MISC_EXPENSE(HOA,INSURANCE,REPAIR)" % (ANNUAL_MISC_EXPENSE / ANNUAL_TOTAL_EXPENSE * 100, ANNUAL_MISC_EXPENSE/MONS_PER_YR)

    print "MONTHLY_EFFECTIVE_RENT: +$%d" % MONTHLY_EFFECTIVE_RENT


    # into-pocket|cash flow
    print "CASH_FLOW: $%d/mon, $%d/yr" % (MONTHLY_NET_INCOME, ANNUAL_NET_INCOME)
    print "CAP_RATE: %.2f%%, %.2fyrs" % (CAP_RATE, 100/CAP_RATE)
    print "CASH_ON_CASH_RETURN: %.2f%%, %.2fyrs" % (CASH_ON_CASH_RETURN, 100/CASH_ON_CASH_RETURN)


if __name__ == '__main__':
    main()
