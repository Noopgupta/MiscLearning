# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize
# your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


# prices = [7, 1, 5, 3, 6, 4]
# prices = [2, 4, 1]
prices = [3, 2, 6, 5, 0, 3]  # dict overwriting the 1st value of 3, so not working for this scenario
dict_prices = {value: index for index, value in enumerate(prices)}
print(dict_prices)

sorted_price = sorted(prices)
print(sorted_price)
l = len(sorted_price)-1

print(dict_prices[sorted_price[0]] , dict_prices[sorted_price[l]])
i = 0
j = l
pos_small = 0
pos_big = 0
profit = 0

# [3, 2, 6, 5, 0, 3]
# [0, 2, 3, 3, 5, 6]

while i <= j:
    pos_small = dict_prices[sorted_price[i]]
    pos_big = dict_prices[sorted_price[j]]
    if pos_small > pos_big:
        j -= 1
        profit = sorted_price[j] - sorted_price[i]
    elif pos_small >= pos_big and i == j:
        i += 1
        j = l
    else:
        print(pos_small, pos_big, i, j)
        profit = sorted_price[j] - sorted_price[i]
        break

print(profit)
