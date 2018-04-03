class Solution(object):
	def findNumberOfLIS(self, nums):
		# time: O(n^2)
		# space: O(n)
		dp, longest = [[1,1] for i in range(len(nums))], 1
		for i, num in enumerate(nums):
			curr_longest, count = 1, 0
			for j in range(i):
				if num > nums[j]:
					curr_longest = max(curr_longest, dp[j][0] + 1)
			for j in range(i):
				if dp[j][0] == curr_longest - 1 and nums[j] < num:
					count+=dp[j][1]
			dp[i] = [curr_longest, max(count, dp[i][1])] ##
			longest = max(longest, curr_longest)
		return sum([item[1] for item in dp if item[0] == longest])


