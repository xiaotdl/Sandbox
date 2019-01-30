#!/usr/bin/env python
import collections

NA = 0
UNKNOWN = 'N/A'

# PAYEE
GOV = 'Government'
HOA = 'HOA'
MERIWEST = 'Meriwest Credit Union'
CHASE = 'JPMorgan Chase Bank'
FARMERS = 'Farmers Insurance'
BASS = 'Bass Insurance'
GAS_STATION = 'Chevron|Shell'
COMCAST = 'Comcast'
PGNE = 'PG&E'
ATNT = 'AT&T'
GARDENER1 = 'Tony Ngvyen'
GARDENER2 = 'TBD'
SC_UTILITY = 'Santa Clara Utility'
COUNTY_UTILITY = 'County Utility'
SUPERMARKET = '99 Ranch|Costco|Safeway|Target|Walmart'
STORE = 'Online|Amazon'
AMAZON = 'Amazon'
NETFLIX = 'Netflix'
MOVIEPASS = 'MoviePass'
NEST = 'Nest'
LANDLORD = 'Landlord'
KINDERGARTEN = 'BB Tree Kindergarten'
BABY_GYM = 'Baby Gym'
BMW_DEALER = "BMW Dealer"


def _yearly(table):
    return [[row[0], row[1], 12*row[2], row[3]] for row in table]


def _percentage(table, total):
    return [[row[0], row[1], row[2]/12, row[2], float("%.2f"%(float(row[2])/float(total)*100)), row[3]] for row in table]

# convert [[name, type, amount, payto]]
# into    [[tag, amount($/mon), amount($/yr), percentage(%)]]
def _tag(table, total):
    tag2amount = collections.defaultdict(int)
    for r in table:
        name = r[0]
        amount = r[2]
        if "@" in name:
            tag = name.split("@")[1]
            tag2amount[tag] += amount
        else:
            raise "Please tag the name!"

    output_table = []
    for tag, amount in tag2amount.items():
        output_table.append([tag, int(amount/12), amount, float("%.2f"%(float(amount)/float(total)*100))])
    output_table.sort(key=lambda r: r[2], reverse=True) # sort by yr amount, in decreasing order
    return output_table


def yearly_bill():
    return [
        # name, type, amount, payto
        ['property_tax@jackson', 'house', 5539+6419, GOV],
        ['home_insurance@jackson', 'house', 781, FARMERS],
        ['gardening@jackson', 'service', 200, GARDENER1], # tree trimming

        ['property_tax@cactus_rose', 'house', 5100, GOV],
        ['hoa@cactus_rose', 'house', 400, HOA],
        ['home_insurance@cactus_rose', 'house', 1147, BASS],
        ['gardening@cactus_rose', 'service', 200, GARDENER2], # tree trimming

        ['property_tax@lake_hollow', 'house', 4800, GOV],
        ['hoa@lake_hollow', 'house', 400, HOA],
        ['home_insurance@lake_hollow', 'house', 1106, FARMERS],
        ['gardening@lake_hollow', 'service', 200, GARDENER2], # tree trimming

        # ['car_registration@camry', 'car', 300, GOV],
        ['car_registration@bmwX5', 'car', 650, GOV],
        ['car_maintainance@bmwX5', 'car', 500+1000, BMW_DEALER],
        ['car_guarantee@bmwX5', 'car', int(5000/4), BMW_DEALER],

        # ['amazon_prime', 'membership', 50, AMAZON],

        # ['nest_indoor_cam', 'membership', 50, NEST],
    ]

def monthly_bill():
    return [
        # name, type, amount, payto
        ['house_loan@jackson', 'house', 3208, MERIWEST],
        # ['internet@jackson', 'utility', 50, ATNT],
        # ['water&refuse@jackson', 'utility', 150, SC_UTILITY],
        # ['electricity@jackson', 'utility', 50, SC_UTILITY],
        # ['gas@jackson', 'utility', 20, PGNE],
        ['lawn@jackson', 'service', 40, GARDENER1],

        ['house_rent@lido', 'house', 2500, LANDLORD],
        ['internet@lido', 'utility', 45, COMCAST],
        # ['power&water&refuse@lido', 'utility', 150, COUNTY_UTILITY],
        ['electricity@lido', 'utility', 50, COUNTY_UTILITY],
        ['gas@lido', 'utility', 20, PGNE],
        # ['lawn@lido', 'service', 40, GARDENER1],

        ['house_loan@cactus_rose', 'house', 685, CHASE],
        ['internet@cactus_rose', 'utility', 50, ATNT],
        ['water&refuse@cactus_rose', 'utility', 100, COUNTY_UTILITY],
        ['electricity@cactus_rose', 'utility', 100, COUNTY_UTILITY],
        ['gas@cactus_rose', 'utility', 70, PGNE],
        ['lawn@cactus_rose', 'service', 35, GARDENER2], # bi-weekly

        ['house_loan@lake_hollow', 'house', 645, CHASE],
        ['internet@lake_hollow', 'utility', 50, ATNT],
        ['water&refuse@lake_hollow', 'utility', 100, COUNTY_UTILITY],
        ['electricity@lake_hollow', 'utility', 100, COUNTY_UTILITY],
        ['gas@lake_hollow', 'utility', 60, PGNE],
        ['lawn@lake_hollow', 'service', 35, GARDENER2], # bi-weekly

        # ['car_insurance@camry', 'car', int(539/6), FARMERS],
        # ['car_gas@camry', 'car', 150, GAS_STATION],
        ['car_insurance@bmwX5', 'car', int(851/6), FARMERS],
        ['car_gas@bmwX5', 'car', 180, GAS_STATION],

        ['phone@xiaotian', 'phone', 35, ATNT],
        ['phone@wendi', 'phone', 35, ATNT],

        # ['netflix', 'entertainment', 10, NETFLIX],

        # ['moviepass(Xiaotian)', 'entertainment', 8, MOVIEPASS],
        # ['moviepass(Wendi)', 'entertainment', 8, MOVIEPASS],

        ['kindergarten@chloe', 'education', 1600, KINDERGARTEN],
        # ['gym(Chloe)', 'education', 80, BABY_GYM],
    ]

def monthly_living_expense():
    return [
        # name, type, amount, payto
        # ['', 'groceries', NA, SUPERMARKET],
        # ['', 'restaurant', NA, RESTAURANT],
        ['food&dining@family', 'food&dining', 1300, UNKNOWN],
        ['shopping@family', 'shopping', 500, STORE],
        ['entertainment@family', 'entertainment', 200, UNKNOWN],
    ]

def show(table, header=['name', 'type', 'amount($)', 'payto']):
    table.insert(0, header)
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
            elif isinstance(table[i][j], float):
                formatted_float = "%.2f" % table[i][j]
                padding = (max_col_lens[j] - 2 - len(formatted_float)) * ' '
                line.append(' ' + padding + formatted_float + ' ')
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

    print 'expense items:'
    show(
        _percentage(
            yearly_bill() + _yearly(monthly_bill()) + _yearly(monthly_living_expense()),
            yearly_total),
        header=['name', 'type', 'amount($/mon)', 'amount($/yr)', 'percentage(%)', 'payto'])
    print

    print 'expense items group by tag:'
    show(
        _tag(
            yearly_bill() + _yearly(monthly_bill()) + _yearly(monthly_living_expense()),
            yearly_total),
        header=['tag', 'amount($/mon)', 'amount($/yr)', 'percentage(%)'])
    print



if __name__ == '__main__':
    main()
