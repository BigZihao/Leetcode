
class Solution(object):

# 时间复杂度: O(n^2 ~ n^3) 空间复杂度 O(n)

	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: Set[str]
		:rtype: bool
		"""
		n = len(s)
		dp = [False] * (n + 1)
		dp[0] = True
		for i in range(n):
			for j in range(i, -1, -1):
				if dp[j] and s[j:i+1] in wordDict:
					dp[i + 1] = True
					break ### saves more time 
		return dp[n]


	def wordBreak2(self, s, wordDict):
		d = [False] * len(s)
		for i in range(len(s)):
			for w in wordDict:
				if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i - len(w) == -1):
					d[i] = True
		return d[-1]


## ok[i] tells whether s[:i] can be built.
	def wordBreak3(self, s, wordDict):
		ok = [True]
		for i in range(1, len(s) + 1):
			ok+= any(ok[j] and s[j:i] in wordDict for j in range(i)),
		return ok[-1]


if __name__ == "__main__":
	assert Solution().wordBreak("leetcode", {"leet", "code"}) == True

