

def minPathSum(self, grid):
	"""
	:type: grid: List[List[int]]
	:rtype: int
	"""
	dp = grid
	m = len(grid)
	n = len(grid[0])
	for i in range(m):
		for j in range(n):
			dp[i][j] = min(dp[i-1][j] + dp[i][j],  dp[i][j-1] + dp[i][j])
	return dp[-1][-1]