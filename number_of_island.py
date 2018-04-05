### related questionsLL

### max area of island, friend circle

## all DFS
## topological sort, detech cycle, stack, recursion


class Solution(object):
    def numberofIsland(self, grid):
        """
        """
        ## cause we dont want to keep grid in recursion
        ## word search is just search, but here we will change the grid
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
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
## Iterate through each of the cell and if it is an island, do dfs to mark all adjacent islands, then increase the counter by 1.

    def numIslands2(self, grid):
        if not grid:
            return 0
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return   ###backtracking, important to exit the dfs
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)



if __name__=="__main__":
    grid = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]
    print(Solution().numberofIsland(grid))

