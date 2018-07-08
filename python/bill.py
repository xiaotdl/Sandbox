NA = 0
UNKNOWN = 'N/A'

# PAYEE
GOV = 'Government'
MERIWEST = 'Meriwest Credit Union'
FARMERS = 'Farmers Insurance'
GAS_STATION = 'Chevron|Shell'
COMCAST = 'Comcast'
PGNE = 'PG&E'
ATNT = 'AT&T'
GARDENER = 'Tony Ngvyen'
SC_UTILITY = 'Santa Clara Utility'
SUPERMARKET = '99 Ranch|Costco|Safeway|Target|Walmart'
STORE = 'Online|Amazon'
AMAZON = 'Amazon'


def yearly_bill():
    return [
        # name, type, amount, payto
        ['property_tax#1793', 'house', 5539+6419, GOV],
        ['home_insurance#1793', 'house', 270, FARMERS],

        ['car_registration#camry', 'car', 300, GOV],

        ['amazon_prime', 'membership', 50, AMAZON],
    ]

def monthly_bill():
    return [
        # name, type, amount, payto
        ['house_loan#1793', 'house', 3208, MERIWEST],

        ['internet', 'utility', 80, COMCAST],
        ['power&water&refuse', 'utility', 150, SC_UTILITY],
        ['gas', 'utility', 20, PGNE],
        ['lawn&gardening', 'service', 40, GARDENER],

        ['car_insurance#camry', 'car', int(539/6), FARMERS],
        ['gas&fuel#camry', 'car', 100, GAS_STATION],

        ['phone(Xiaotian)', 'phone', 35, ATNT],
        ['phone(Wendi)', 'phone', 35, ATNT],
    ]

def monthly_living_expense():
    return [
        # name, type, amount, payto
        # ['', 'groceries', NA, SUPERMARKET],
        # ['', 'restaurant', NA, RESTAURANT],
        ['', 'food&dining', 1300, UNKNOWN],
        ['', 'shopping', 500, STORE],
        ['', 'entertainment', 200, UNKNOWN],
    ]

def show(table):
    table.insert(0, ['name', 'type', 'amount($)', 'payto'])
    max_col_lens = [0 for x in range(len(table[0]))]
    for c in range(len(table[0])):
        for r in range(len(table)):
            max_col_lens[c] = max(max_col_lens[c], len(str(table[r][c])) + 2)

    dilimited_line = '+' + '+'.join(['-'*x for x in max_col_lens]) + '+'
    print dilimited_line
    for i in range(len(table)):
        line = []
        for j in range(len(table[i])):
            padding = (max_col_lens[j] - 2 - len(str(table[i][j]))) * ' '
            if isinstance(table[i][j], int):
                line.append(' ' + padding + str(table[i][j]) + ' ')
            else:
                line.append(' ' + str(table[i][j]) + padding + ' ')
        print '|' + '|'.join(line) + '|'
        if i == 0:
            print dilimited_line
    print dilimited_line


def main():
    show(monthly_bill())
    monthly_bill_sum = sum(item[2] for item in monthly_bill())
    print 'monthly_bill_sum:', monthly_bill_sum
    print


    show(monthly_living_expense())
    monthly_living_expense_sum = sum(item[2] for item in monthly_living_expense())
    print 'monthly_living_expense_sum:', monthly_living_expense_sum
    print


    show(yearly_bill())
    yearly_bill_sum = sum(item[2] for item in yearly_bill())
    print 'yearly_bill_sum:', yearly_bill_sum
    print

    print '~' * 50

    monthly_total = monthly_bill_sum + monthly_living_expense_sum + int(yearly_bill_sum/12)
    print 'monthly total:', monthly_total

    yearly_total = 12 * monthly_total
    print 'yearly total:', yearly_total



if __name__ == '__main__':
    main()
