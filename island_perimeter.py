class Solution(object):
	def islandPerimeter(self, grid):
		grid_ext = ['0' + ''.join(str(x) for x in row) + '0' for row in grid]
		grid_trans = list(map(list, zip(*grid)))
		grid_ext+= ['0' + ''.join(str(x) for x in row) + '0' for row in grid_trans]
		return sum(row.count('01') + row.count('10') for row in grid_ext)

	def islandPerimeter2(self, grid):
		perimeter = 0
		gridRows  = len(grid)
		if gridRows == 0:
			return 0
		gridCols = len(grid[0])
		for i in range(gridRows):
			for j in range(gridCols):
				if grid[i][j] == 1:
					perimeter+=4
					if i > 0 and grid[i-1][j]:
						perimeter-=1
					if j > 0 and grid[i][j-1]:
						perimeter-=1
					if i+1 < gridRows and grid[i+1][j]:
						perimeter-=1
					if j+1 < gridCols and grid[i][j+1]:
						perimeter-=1
		return perimeter

assert Solution().islandPerimeter2([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16