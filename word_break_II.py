

wordbreak II is dp + dfs
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        self.dfs(s, wordDict, '', res)
        return res
    
    def check(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i, -1, -1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i + 1] = True
                    break ### saves more time 
        return dp[n]
    
    def dfs(self, s, wordDict, path, res):
        if self.check(s, wordDict):
            if len(s) == 0:
                res.append(path[1:])
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, path + ' ' + s[:i], res)






                    

class Solution(object):
    def wordBreak(self, s, wordDict):
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res


    def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    #running time: O(mn^2), n = len(s), m = len(wordDict)
    """
    Let‘s say the average word length in wordDict is k,
    so it takes n/k times to reach end.
    Each time, the helper function would be called and it's running time is O(m*n)
    So the whole runinng time  would be O( m*n*n/k), which is O(m*n^2)
    """
        dic={}
        
        def helper(s):
            if not s: return [None]
            if s in dic: return dic[s]
            res =[]
            for word in wordDict:
                n = len(word)
                if word == s[:n]:
                    for each in helper(s[n:]):
                        if each:res.append(word+" "+each)
                        else: res.append(word)
                dic[s] = res
            return res
        
        return helper(s)
 
