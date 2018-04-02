class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		free = 0
		have = cool = float('-inf')
		for p in prices:
			free, have, cool = max(free, cool), max(have, free - p), have + p
		return max(free, cool)
