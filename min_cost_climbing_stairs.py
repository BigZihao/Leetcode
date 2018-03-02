class Solution(object):
	def minCostClimbingStairs(self, cost):
		n = len(cost)
		if n == 0 or n== 1:
			return 0
		min_cost0, min_cost1 = cost[0], cost[1]
		for i in range(2, n):
			min_cost0,  min_cost1 = min_cost1, min(min_cost1, min_cost0) + cost[i]
		return min(min_cost0, min_cost1)