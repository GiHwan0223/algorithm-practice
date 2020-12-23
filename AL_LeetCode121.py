import sys
prices = [7,1,5,3,6,4]

def maxProfit(prices):
  profit = 0
  minPrice = sys.maxsize

  for value in prices:
    minPrice = min(value, minPrice)
    profit = max(profit, value - minPrice)
  return profit

print(maxProfit(prices))
