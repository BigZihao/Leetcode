string

给定一个长度为 n 的 String，切成若干个 pieces 总共有 $$2^{n-1}$$ 种切法，即对于所有 $$n-1$$ 个分界点上，选择“切/不切”.

此类问题最常用的优化，就是利用子串性质， abuse 子串的结构。
同时维护一个类似 sliding window and two pointer/ hashtable 的结构去向尾部移动，如果是 KMP pattern matching，不回滚的 window / pattern 就可以达到 linear time.

longest substring without repeating substring
hashtable + sliding window

keep two pinter, start and end, and also keep a number of lastcount
def countBinarySubstring(self, s):
	n = len(s)
	res = 0
	start = 0
	lastcount = 1
	for i in range(1, n):
		if s[i]!=s[i-1]:
			res+=1
			lastcount = i-start
			start = i
		else:
			if i-start<lastcount:
				res+=1
	return res


def repeatedSubstringPattern(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if not str:
        return False
        
    ss = (s + s)[1:-1]
    return s in ss

Find all anagrams in a string 


def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    start = 0
    dics = {}
    dicp = {}
    res = []
    lp= len(p)
    for i in p:
        dicp[i] = dicp.get(i, 0) +1
    for i, string in enumerate(s):
        if i+1-start>lp:
            dics[s[start]]-=1
            if dics[s[start]] == 0:
                del dics[s[start]]
            start+=1
        dics[string] = dics.get(string, 0) + 1
        if dics == dicp:
            res.append(start)
    return res