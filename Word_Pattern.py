热手题，对于 bijection mapping 就是两个 hashmap 互相查，和 Isomorphic Strings 一样。

class Solution(object):
	def wordPattern(self, pattern, str):
		str = str.split(" ")
		return len(set(str)) == len(set(pattern)) == len(set(zip(str, pattern))) and len(pattern) == len(str)

	def wordPattern2(self, pattern, str):
		str = str.split(" ")
		if len(pattern)!=len(str):
			return False

		pattern_map, str_map = {}, {}
		for i in range(len(pattern)):
			if pattern_map.get(pattern[i], -1)!=str_map.get(str[i], -1):
				return False
			pattern_map[pattern[i]] = str_map[str[i]] = i

		return True


if __name__ == "__main__":
	print( Solution().wordPattern("aba","dog cat dog cat") )
	print( Solution().wordPattern2("aba","dog cat dog cat") )