class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        if n == 0 or m== 0:
            return 0
        dp = grid
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j]+=dp[i][j-1]
                elif j == 0:
                    dp[i][j]+=dp[i-1][j]
                else:
                    dp[i][j]+=min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


## dp and recursion are so correlated

    def minPathSum(self, grid):
        if not len(grid) or not len(grid[0]):
            return 0

        m, n, cache = len(grid) - 1, len(grid[0]) - 1, {}

        return self.findMinSum(grid, m, n, cache)

    def findMinSum(self, grid, m, n, cache):
        if (m, n) in cache:
            return cache[(m, n)]
        elif m < 0 or n < 0:
            return float('inf')
        elif m == 0 and n == 0:
            return grid[0][0]
        else:
            cache[(m, n)] = grid[m][n] + min(self.findMinSum(grid, m - 1, n, cache), self.findMinSum(grid, m, n - 1, cache))

            return cache[(m, n)]