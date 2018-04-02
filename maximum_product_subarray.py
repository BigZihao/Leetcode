class Solutions(object):
	def maximumProductSubarray(self, nums):
		maximum = float('-inf')
		curMax, curMin = 1, 1
		for i in range(nums):
			curMax, curMin = max(i, curMax*i, curMin*i) , min(i, curMin*i, curMax*i)
			maximum = max(maximum, curMax)
		return maximum