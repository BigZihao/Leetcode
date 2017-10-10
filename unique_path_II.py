
def uniquePathsWithObstacles(self, obstacleGrid):
	"""
	:type obstacleGrid: List[List[int]]
	:rtype: int
	"""
	if obstacleGrid[0][0]==1:
		return 0
	m = len(obstacleGrid)
	n = len(obstacleGrid[0])
	dp = [[0 for _ in range(n)] for _ in range(m)]

	## set up the initial value for dp
	dp[0][0] = 1
	for i in range(1, m):
		dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
	for j in range(1, n):
		dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
	
	## transfer function 
	for i in range(1, m):
		for j in range(1, n):
			if obstacleGrid[i][j]==1:
				dp[i][j] = 0
			else:
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
	return dp[-1][-1]



