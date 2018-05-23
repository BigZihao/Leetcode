class Solution():
	def spiralOrder(self, matrix):
		if not matrix or not matrix[0]:
			return []
		ans = []
		n, m = len(matrix), len(matrix[0])
		u, d, l, r = 0, n-1, 0, m-1
		while u<d and l<r:
			ans+=[matrix[u][j] for j in range(l, r)]
			ans+=[matirx[i][r] for i in range(u, d)]
			ans+=[matrix[d][j] for j in range(r, l, -1)]
			ans+=[matrix[i][l] for i in range(d, u, -1)]
			u, d, l, r = u+1, d-1, l+1, r-1
		if l == r:
			ans+=[matrix[i][r] for i in range(u, d+1)]
		elif u == d:
			ans+=[matrix[u][j] for j in range(l, r+1)]
		return ans