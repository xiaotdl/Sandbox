# google t4
stats = [
    # base, stock, signon
    [15.5, 34, 5],
    [15.7, 33, 3],
    [17, 45, 2],
    [14, 48, 5],
    [14.5, 37.5, 5],
    [16.4, 38, 10],
    [15.8, 32, 5],
    [16, 35, 5],
    [16.4, 38, 10]
]

base = [stat[0] for stat in stats]
stock = [stat[1] for stat in stats]
signon = [stat[2] for stat in stats]

def getAvgMinMax(l):
    return [round(sum(l)/float(len(l)), 2), round(min(l), 2), round(max(l), 2)]

mma_base = getAvgMinMax(base)
mma_stock = getAvgMinMax(stock)
mma_signon = getAvgMinMax(signon)
mma_total = getAvgMinMax([base[i]*1.15 + stock[i]/4 + signon[i]/4 for i in range(len(stats))])

print "sample size: " + str(len(stats))
print "category: [avg, min, max]"
print "base:   " + str(mma_base)
print "stock:  " + str(mma_stock)
print "signon: " + str(mma_signon)
print "total:  " + str(mma_total)


