"""
From a series of points on a time sequence that represents stock profit points,
select the times to buy and sell to maximize profits.

Since it is a time series, you can only sell after you have bought.
"""

source = [36,10,3,18,3,7,8,9,6]
profit = {} # d[sum of b - a] = (a, b)

for i in source:
    for j in source[source.index(i)+1:]:
        if j > i:
            profit[j - i] = (i, j)
                
buy, sell = profit[max(profit.keys())]
print("Buy at {b} and sell at {s}.".format(b=buy, s=sell))
        
        
