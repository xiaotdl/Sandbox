address = "example address"
link = "example link"
description = """
example description
"""

# == invest/out-of-pocket ==
purchase_price = 1000000 # USER_INPUT

downpay_percent = 20.00/100 # DEFAULT: 20.00%

est_closing_cost = 2.00/100 * purchase_price # DEFAULT: 2.00% * purchase_price


# == financing/out-of-pocket ==
mortgage_loan_yrs = 30 # DEFAULT: 30yrs
est_mortgage_loan_apr = 4.50/100 # DEFAULT: 4.50%


# == tax/out-of-pocket ==
property_tax_rate = 1.50/100 # DEFAULT: 1.50%


# == expense/out-of-pocket ==
est_monthly_hoa_expense = 0 # DEFAULT: 0

est_annual_home_insurance_expense = 0.05/100 * purchase_price # DEFAULT: 0.05% * purchase_price

est_annual_repair_reserve_expense = 1.00/100 * purchase_price # DEFAULT: 1.00% * purchase_price


# == income/into-pocket ==
est_vacancy_percent = 5.00/100 # DEFAULT: 5.00%

est_monthly_rent = 2400 # USER_INPUT

# == service/out-of-pocket ==
est_annual_property_manager_service_fee_rate = 6.00/100 # DEFAULT: 6.00%

est_annual_lawn_service_fee = 50 * 12 # DEFAULT: 600
