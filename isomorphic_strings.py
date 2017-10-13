
class Solution(object):
	def isIsomorphic1(self, s, t):
		d1, d2 = {}, {}
		for i, val in enumerate(s):
			d1[val] = d1.get(val, []) + [i]
		for i, val in enumerate(t):
			d2[val] = d2.get(val, []) + [i]
		return sorted(d1.values()) == sorted(d2.values())

	def isIsomorphic2(self, s, t):
		return len(set(s)) == len(set(zip(s,t))) == len(set(t))


if __name__ == "__main__":
	print(Solution().isIsomorphic1("egg","add"))
	print(Solution().isIsomorphic2("egg","add"))