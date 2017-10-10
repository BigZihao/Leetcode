
class Solution(object):
	def minumumTotal(self, triangle):
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""
		n = len(triangle)
		dp = triangle[-1]
		for i in range(n - 2, -1, -1):
			for j in range(i+1):
				dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
		return dp[0]


if __name__ == "__main__":
	assert Solution().minumumTotal([
		[2],
		[3,4],
		[6,5,7],
		[4,1,8,3]
		]) == 11
	print("done")