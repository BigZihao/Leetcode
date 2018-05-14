class Solution():
    def isOneEditDistance(self, s, t):
        ls, lt = len(s), len(t)
        if ls>lt:
            return self.isOneEditDistance(t, s)
        if lt - ls >1 or s == t:
            return False
        for i in range(ls):
            if s[i] !=t[i]:
                return s[i+1:] == t[i+1:] or s[i:] == t[i+1:]
        return True


## two pointer 
    def isOneEditDistance(self, s, t):
        n, m = len(s), len(t)
        if abs(n - m) > 1:
            return False
        k = min(n, m)
        i = j = 0
        while i < k and s[i] == t[i]:
            i += 1
        while j < k - i and s[~j] == t[~j]:
            j += 1
        return max(n, m) - (i + j) == 1
