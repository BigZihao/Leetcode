
class Solution(object):
	def minumumTotal(self, triangle):
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""
        if not triangle:
            return 0
        dp = triangle[-1]
        height = len(triangle)
        for row in range(height-2, -1, -1):
            for j in range(row+1): ## each element in the row
                dp[j] = triangle[row][j] + min(dp[j], dp[j+1])
        return dp[0]

if __name__ == "__main__":
	assert Solution().minumumTotal([
		[2],
		[3,4],
		[6,5,7],
		[4,1,8,3]
		]) == 11
	print("done")