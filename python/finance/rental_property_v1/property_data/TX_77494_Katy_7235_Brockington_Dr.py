address = "7235 Brockington Dr, Katy, TX 77494"
link = "https://www.redfin.com/TX/Katy/7235-Brockington-Dr-77494/home/32881345"
description = """
MUST SEE!!!! Amazing 4 bedroom 2 bathroom, Family room with beautiful tile, great ligthing and wood in all 4 bedrooms, a cozy fireplace. Master suite is a retreat w/ large walk-in closet & wall of windows. Master bath has a garden tub, separate shower & dual vanities. This home also provides a formal dining room and a breakfast area Walking distance to school, playground and shoping!
"""

# == invest/out-of-pocket ==
purchase_price = 215000 # USER_INPUT

downpay_percent = 20.00/100 # DEFAULT: 20.00%

# est_closing_cost = 2.00/100 * purchase_price # DEFAULT: 2.00% * purchase_price
est_closing_cost = 6000 / 5


# == financing/out-of-pocket ==
mortgage_loan_yrs = 30 # DEFAULT: 30yrs
est_mortgage_loan_apr = 4.5 /100 # DEFAULT: 4.50%


# == tax/out-of-pocket ==
property_tax_rate = 2.69/100 # DEFAULT: 1.50%


# == expense/out-of-pocket ==
est_monthly_hoa_expense = 33 # DEFAULT: 0

# est_annual_home_insurance_expense = 0.05/100 * purchase_price # DEFAULT: 0.05% * purchase_price
est_annual_home_insurance_expense = 100 * 12

est_annual_repair_reserve_expense = 50 * 12


# == income/into-pocket ==
est_vacancy_percent = 0.00/100 # DEFAULT: 5.00%

# est_monthly_rent = 1700 # USER_INPUT
est_monthly_rent = 1800 # USER_INPUT

# == service/out-of-pocket ==
est_annual_property_manager_service_fee_rate = 8.33/100 # DEFAULT: 6.00%

# est_annual_lawn_service_fee = 30 * 12 # DEFAULT: 600
est_annual_lawn_service_fee = 0
