class Solution(object):
	## standard dp solutions space O(n^2)
	def longestPalindromeSubseq(self, s):
		if s == s[::-1]:
			return len(s)

		n = len(s)
		dp =[[0 for j in range(n)] for i in range(n)]

		for i in range(n-1, -1, -1):
			dp[i][i] = 1
			for j in range(i+1, n):
				if s[i] == s[j]:
					dp[i][j] = 2 + dp[i+1][j-1]  ## dp[i+1][j-1] is a condition in longest palindrome
				else:
					dp[i][j] = max(dp[i+1][j], dp[i][j-1])
					## the transition for sequence

		return dp[0][n-1]
		

	def longestPalindromeSubseq(self, s):
		n = len(s)
		dp = [1]*n
		for j in range(1, n):
			pre = dp[j]
			for i in reversed(range(0, j)):
				tmp = dp[i]
				if s[i] == s[j]:
					dp[i] = 2 + pre if i+1<j-1 else 2
				else:
					dp[i] = max(dp[i+1], dp[i])
				pre = tmp
		return dp[0]

