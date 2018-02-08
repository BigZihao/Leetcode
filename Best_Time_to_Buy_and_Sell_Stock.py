##Best Time to Buy and Sell Stock

def maxProfit(self, prices):
	n = len(prices)
	if n<=1:
		return 0
	max_profit = 0
	low_price = prices[0]
	for i in range(1, n):
		low_price = min(prices[i], low_price)
		max_profit = max(max_profit, prices[i] - low_price)
	return max_profit