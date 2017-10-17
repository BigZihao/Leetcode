

class Solution(object):
	def firstUniqChar(self, s):
		dic = {}
		for i in s:
			if i not in dic:
				dic[i] = 1
			else:
				dic[i]+=1
		for i in range(len(s)):
			c = s[i]
			if dic[c] == 1:
				return i
		return -1

	def firstUniqChar2(self, s):
		letters = 'abcdefghijklmnopqrstuvwxyz'
		index = [s.index(l) for l in letters if s.count(l) == 1]
		return min(index) if len(index)!=0 else -1





if __name__ == "__main__":
	print(Solution().firstUniqChar("loveleetcode"))
	print(Solution().firstUniqChar2("loveleetcode"))