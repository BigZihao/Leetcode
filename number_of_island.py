### related questionsLL

### max area of island, friend circle

## all DFS
## topological sort, detech cycle, stack, recursion


class Solution(object):
	def numberofIsland(self, grid):
		"""
		"""
		m, n = len(grid), len(grid[0])
		def sinkDFS(i, j):
			if 0<=i < m and 0<=j < n and grid[i][j] == '1':
				grid[i][j] = '0'
				sinkDFS(i,j+1)
				sinkDFS(i, j-1)
				sinkDFS(i+1, j)
				sinkDFS(i-1, j)
				#### map won't work in this situation
		res = 0
		for i in range(m):
			for j in range(n):
				res+= int(grid[i][j])
				sinkDFS(i,j)
		return res


if __name__=="__main__":
	grid = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]
	print(Solution().numberofIsland(grid))

