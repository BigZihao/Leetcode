

class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		last, now = 0, 0
		for i in nums:
			last, now = now, max(last + i, now)
			return now

if __name__ == "__main__":
	assert Solution().rob([1,2,4,5,3,3,3,1,34,62,9])