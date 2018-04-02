class Solution(object):
    def numSquares(self, n):
        if n < 2:
            return n
        lst = []
        i = 1
        while i*i <= n:
            lst.append(i*i)
            i+=1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt+=1
            tmp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x<y:
                        break
                    tmp.add(x-y)
            toCheck = tmp
        return cnt

    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

    def numSquares(self, n):
        s = [i*i for i in range(1, int(math.sqrt(n)) + 1)]
        l = 0
        currentLevel = [0]

        while True:
            nextLevel = []
            for a in currentLevel:
                for b in s:
                    if a+b == n: return l+1
                    if a+n<n: nextLevel.append(a+b)
            currentLevel = list(set(nextLevel))
            l+=1
