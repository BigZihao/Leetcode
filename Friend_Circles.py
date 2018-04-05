class Solution(object):
	def friendCircle(self, M):
		"""
		"""
		N = len(M)
		visited = [False]*N
		res = 0
		for i in range(N):
			if visited[i]:
				continue
			stack = [i]
			visited[i] = True
			while stack:
				x = stack.pop()
				for y in range(N):
					if not visited[y] and M[x][y] == 1:
						visited[y] = True
						stack.append(y)
			res+= 1
		return res

	def findCircleNum2(self, M):
		"""
		:type M: List[List[int]]
		:rtype: int
		"""
		n = len(M)
		visited = [False]*n
		def dfs(M, curr, n, visited):
			visited[curr]=True
			for i in range(n):
				if M[curr][i]==1 and visited[i]==False:
					visited[i]=True
					dfs(M, i, n, visited)
		ans = 0
		for i in range(n):
			if visited[i]:
				continue
			dfs(M, i, n, visited)
			ans+=1
		return ans

	def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = 0
        n = len(M)
        people = [0]*n
            
        def dfs(i):
            people[i]=1
            for j in range(n):
                if M[i][j] ==1 and people[j]==0:
                    people[j]=1
                    dfs(j)
                    ## be careful with the exit condition
        
        for i in range(n):
            if people[i]==0:
                count+=1
                dfs(i)
        return count


## the important difference is that we need to check all friends instead of the direct neighbors

if __name__ == "__main__":
	M = [[1,1,0],[1,1,1],[0,1,1]]
	print(Solution().friendCircle(M))
	print(Solution().findCircleNum2(M))
