
def uniquePaths(self, m, n):
	aux = [[1 for i in range(m)] for j in range(n)]
	for i in range(m):
		for j in range(n):
			aux[i][j] = aux[i-1][j] + aux[i][j-1]
	return aux[-1][-1]