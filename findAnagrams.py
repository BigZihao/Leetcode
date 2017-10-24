class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        lp = len(p)
        for i in range(len(s)):
            if sorted(s[i:i+lp]) == sorted(p):
                res.append(i)
        return res
    ## but using sort is very expensive, it is nplog(p)


    ## Maintain a window of len(p) in s, and slide to right until finish. Time complexity is O(len(s))

    def findAnagrams1(self, s, p):
        ls, lp = len(s), len(p)
        cp = collections.Counter(p)
        cs = collections.Counter()
        ans = []
        for i in range(ls):
            cs[s[i]]+=1
            if i >= lp:
                cs[s[i-lp]]-=1
                if cs[s[i-lp]] == 0:
                    del cs[s[i - lp]]
            if cs == cp:
                ans.append(i - lp + 1)
        return ans
    
    def findAnagrams12(self, s, p):
        ls, lp = len(s), len(p)
        ## Counter is dictionary
        cp = {}
        for i in p:
            cp[i] = cp.get(i, 0) + 1
        cs = {}
        ans = []
        for i in range(ls):
            cs[s[i]]= cs.get(s[i], 0) + 1
            if i >= lp:
                cs[s[i-lp]]-=1
                if cs[s[i-lp]] == 0:
                    del cs[s[i - lp]]
            if cs == cp:
                ans.append(i - lp + 1)
        return ans


    ## O(n)
    ## 字典cp记录要凑成目标字符串p的anagram，各字符分别缺多少个  整数count记录凑成目标字符串p一共还缺多少个字符
    def findAnagrams2(self, s, p):
        ls, lp = len(s), len(p)
        count = lp
        cp = collections.Counter(p)
        ans = []
        for i in range(ls):
            if cp[s[i]] >= 1:
                count-=1
            cp[s[i]]-=1
            if i>=lp:
                if cp[s[i-lp]] >= 0:
                    count+=1
                cp[s[i-lp]]+=1
            if count == 0:
                ans.append(i - lp + 1)
        return ans



import collections
if __name__ == "__main__":
    print( Solution().findAnagrams("cbaebabacd", "abc"))
    print( Solution().findAnagrams1("cbaebabacd", "abc"))
    print( Solution().findAnagrams12("cbaebabacd", "abc"))
    print( Solution().findAnagrams2("cbaebabacd", "abc"))