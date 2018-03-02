class Solution(object):
    def longestPalindrome(self, s):
        ## brute force way is O(n^3)

    def longestPalindrome(self, s):
        n = len(s)
        dp = [[0]*n for i in range(n)]
        count = 0
        maxlength=1
        
        for end in range(n):
            dp[end][end] = 1
            count+=1
            for start in range(end):
                if s[start] == s[end] and (start+1>=end-1 or dp[start+1][end-1]) and end-start>maxlength:
                    res = s[start:end]
        return res