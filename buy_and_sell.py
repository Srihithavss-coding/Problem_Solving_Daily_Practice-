"""You are given an array prices where prices[i] is the price of a given stock on the i^th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""


#time complexity: O(n^2) 
def max_profit(prices):
    max_profit = 0 
    prices = prices[::-1]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            sell = prices[i]
            buy = prices[j]
            profit =sell - buy
            if profit > max_profit:
               max_profit =  profit

    return max_profit
print("Maximum profit:", max_profit([7,1,5,3,6,4]))  # Output: 5


#single pass optimal solution
#time complexity: O(n) 

def max_profit(prices):
    min_price = prices[0]
    max_profit = 0 
    for i in range(1, len(prices)):
        if prices[i]<min_price:
            min_price = prices[i]
        else:
            profit = prices[i] - min_price
            if profit>max_profit:
                max_profit = profit

    return max_profit


print("Maximum profit:", max_profit([7,1,5,3,6,4]))  # Output: 5