class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n<=1:
            return s
        dp = [[0]*n for i in range(n)]
        res= ''
        maxlength=1
        for end in range(n):
            dp[end][end] = 1
            for start in range(end+1):
                if s[start] == s[end] and (end-start<=2 or dp[start+1][end-1]):
                    dp[start][end] = 1
                    if end-start+1>=maxlength:
                        res = s[start:end+1]
                        maxlength = end-start+1
        return res