class Solution(object):
	def countSubstrings(self, s):
		"""
		"""
		res = 0
		n = len(s)
		for i in range(n):
			for j in range(i, n):
				if s[i:j] == s[i:j][::-1]
				res+=1
		return res

	## DP O(N*N)
	def countSubstrings(self, s):
		n = len(s)
		dp = [[0]*n for i in range(n)]
		count = 0
		for end in range(n):
			dp[end][end] = 1
			count+=1
			for start in range(end):
				if s[start] == s[end] and (start+1>=end-1 or dp[start+1][end-1]):
					count+=1
					dp[start][end] = 1
		return count