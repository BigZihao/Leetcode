class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            if obstacleGrid[i][0]==1:
                break
            dp[i][0] = 1
        for j in range(m):
            if obstacleGrid[0][j]==1:
                break
            dp[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j]!=1:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]