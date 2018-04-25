## time O(n) space O(1)

class Solutions(object):
	def maximumProductSubarray(self, nums):
		maximum = float('-inf')
		curMax, curMin = 1, 1
		for i in nums:
			curMax, curMin = max(i, curMax*i, curMin*i) , min(i, curMin*i, curMax*i)
			maximum = max(maximum, curMax)
		return maximum