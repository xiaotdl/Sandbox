#!/usr/bin/env python
"""
This script is running numbers and calculate cash flow stats.

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

EST_CLOSING_COST = est_closing_cost

EST_ACTUAL_PURCASE_PRICE = DOWNPAY + EST_CLOSING_COST


# == financing/out-of-pocket ==
MORTGAGE_LOAN = PURCHASE_PRICE - DOWNPAY
MORTGAGE_LOAN_YRS = mortgage_loan_yrs
EST_MORTGAGE_LOAN_APR = est_mortgage_loan_apr
EST_MONTHLY_MORTGAGE_LOAN_PAYMENT = \
    calculate_mortgage_monthly_payment(MORTGAGE_LOAN, MORTGAGE_LOAN_YRS, EST_MORTGAGE_LOAN_APR)
EST_ANNUAL_MORTGAGE_PAYMENT = EST_MONTHLY_MORTGAGE_LOAN_PAYMENT * MONS_PER_YR


# == tax/out-of-pocket ==
PROPERTY_TAX_RATE = property_tax_rate
ANNUAL_PROPERTY_TAX = PURCHASE_PRICE * PROPERTY_TAX_RATE


# == expense/out-of-pocket ==
EST_MONTHLY_HOA_EXPENSE = est_monthly_hoa_expense
EST_ANNUAL_HOA_EXPENSE = EST_MONTHLY_HOA_EXPENSE * MONS_PER_YR

EST_ANNUAL_HOME_INSURANCE_EXPENSE = est_annual_home_insurance_expense

EST_ANNUAL_REPAIR_RESERVE_EXPENSE = est_annual_repair_reserve_expense

EST_ANNUAL_MISC_EXPENSE = \
    EST_ANNUAL_HOA_EXPENSE + \
    EST_ANNUAL_HOME_INSURANCE_EXPENSE + \
    EST_ANNUAL_REPAIR_RESERVE_EXPENSE


# == income/into-pocket ==
EST_VACANCY_PERCENT = est_vacancy_percent

EST_MONTHLY_RENT = est_monthly_rent
EST_MONTHLY_EFFECTIVE_RENT =  EST_MONTHLY_RENT * (1 - EST_VACANCY_PERCENT)

EST_ANNUAL_GROSS_INCOME = EST_MONTHLY_EFFECTIVE_RENT * MONS_PER_YR


# == service/out-of-pocket ==
EST_ANNUAL_PROPERTY_MANAGER_SERVICE_FEE_RATE = est_annual_property_manager_service_fee_rate
EST_ANNUAL_PROPERTY_MANAGER_SERVICE_FEE = EST_ANNUAL_PROPERTY_MANAGER_SERVICE_FEE_RATE * EST_ANNUAL_GROSS_INCOME

EST_ANNUAL_SERVICE_FEE = EST_ANNUAL_PROPERTY_MANAGER_SERVICE_FEE


# == total/out-of-pocket ==
EST_ANNUAL_TOTAL_EXPENSE = \
    EST_ANNUAL_MORTGAGE_PAYMENT + \
    ANNUAL_PROPERTY_TAX + \
    EST_ANNUAL_SERVICE_FEE + \
    EST_ANNUAL_MISC_EXPENSE
EST_MONTHLY_TOTAL_EXPENSE = EST_ANNUAL_TOTAL_EXPENSE / MONS_PER_YR


# == cash flow/into-pocket ==
EST_ANNUAL_NET_INCOME = EST_ANNUAL_GROSS_INCOME - EST_ANNUAL_TOTAL_EXPENSE
EST_MONTHLY_NET_INCOME = EST_ANNUAL_NET_INCOME / MONS_PER_YR


# == metric ==
# Capitalization Rate: return on income to property price
EST_CAP_RATE = EST_ANNUAL_NET_INCOME / PURCHASE_PRICE * 100

# Cash-on-Cash Return: return on income to actual money put in
EST_CASH_ON_CASH_RETURN = EST_ANNUAL_NET_INCOME / EST_ACTUAL_PURCASE_PRICE * 100


def main():
    print "== addr == %s" % address
    print "== link == %s" % link
    print "== desp == %s" % description
    print

    print "== analysis =="
    print "HOUSE_VALUE: $%d" % PURCHASE_PRICE

    # out-of-pocket
    print "EST_OUT_OF_POCKET: $%d" % EST_ACTUAL_PURCASE_PRICE

    # balance sheet
    print "EST_MONTHLY_TOTAL_EXPENSE: -$%d" % EST_MONTHLY_TOTAL_EXPENSE
    print "\t%5.2f%%, %5d - EST_ANNUAL_MORTGAGE_PAYMENT" % (EST_ANNUAL_MORTGAGE_PAYMENT / EST_ANNUAL_TOTAL_EXPENSE * 100, EST_ANNUAL_MORTGAGE_PAYMENT/MONS_PER_YR)
    print "\t%5.2f%%, %5d - ANNUAL_PROPERTY_TAX" % (ANNUAL_PROPERTY_TAX / EST_ANNUAL_TOTAL_EXPENSE * 100, ANNUAL_PROPERTY_TAX/MONS_PER_YR)
    print "\t%5.2f%%, %5d - EST_ANNUAL_SERVICE_FEE" % (EST_ANNUAL_SERVICE_FEE / EST_ANNUAL_TOTAL_EXPENSE * 100, EST_ANNUAL_SERVICE_FEE/MONS_PER_YR)
    print "\t%5.2f%%, %5d - EST_ANNUAL_MISC_EXPENSE" % (EST_ANNUAL_MISC_EXPENSE / EST_ANNUAL_TOTAL_EXPENSE * 100, EST_ANNUAL_MISC_EXPENSE/MONS_PER_YR)

    print "EST_MONTHLY_EFFECTIVE_RENT: +$%d" % EST_MONTHLY_EFFECTIVE_RENT


    # into-pocket|cash flow
    print "EST_CASH_FLOW: $%d/mon, $%d/yr" % (EST_MONTHLY_NET_INCOME, EST_ANNUAL_NET_INCOME)
    print "EST_CAP_RATE: %.2f%%, %.2fyrs" % (EST_CAP_RATE, 100/EST_CAP_RATE)
    print "EST_CASH_ON_CASH_RETURN: %.2f%%, %.2fyrs" % (EST_CASH_ON_CASH_RETURN, 100/EST_CASH_ON_CASH_RETURN)


if __name__ == '__main__':
    main()
