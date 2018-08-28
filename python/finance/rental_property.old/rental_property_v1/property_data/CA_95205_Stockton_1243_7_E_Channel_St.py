address = "1243 7 E Channel St, Stockton, CA 95205"
link = "https://www.redfin.com/CA/Stockton/1243-Channel-St-95205/home/19796557"
description = \
"""
Great investment property with cash flow!
"""

# == invest/out-of-pocket ==
purchase_price = 270000 # USER_INPUT

downpay_percent = 20.00/100 # DEFAULT: 20.00%

est_closing_cost = 2.00/100 * purchase_price # DEFAULT: 2.00% * purchase_price


# == financing/out-of-pocket ==
mortgage_loan_yrs = 30 # DEFAULT: 30yrs
est_mortgage_loan_apr = 4.50/100 # DEFAULT: 4.50%


# == tax/out-of-pocket ==
property_tax_rate = 1.23/100 # DEFAULT: 1.50%


# == expense/out-of-pocket ==
est_monthly_hoa_expense = 0 # DEFAULT: 0

est_annual_home_insurance_expense = 0.05/100 * purchase_price # DEFAULT: 0.05% * purchase_price

est_annual_repair_reserve_expense = 1.00/100 * purchase_price # DEFAULT: 1.00% * purchase_price


# == income/into-pocket ==
est_vacancy_percent = 8.00/100 # DEFAULT: 8.00%

est_monthly_rent = 2000 # USER_INPUT

# == service/out-of-pocket ==
est_annual_property_manager_service_fee_rate = 10.00/100 # DEFAULT: 0.00%
