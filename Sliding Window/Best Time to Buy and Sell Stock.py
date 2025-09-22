def maxProfit(prices):
    max_profit = 0
    minimum_buy = prices[0]
    for sellingPrice in prices:
        max_profit = max(max_profit, sellingPrice - minimum_buy)
        minimum_buy = min(minimum_buy, sellingPrice)
    return max_profit
