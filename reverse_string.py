class Solution(object):
	def reverseString(self, s):
		l = len(s)
		if l < 2:
			return s
		return self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])


	def reverseString2(object, s):
		r = list(s)
		i, j = 0, len(r)-1
		while i<j:
			r[i], r[j] = r[j], r[i]
			i+=1
			j-=1
		return "".join(r)


if __name__ == "__main__":
	print(Solution().reverseString("hello"))
	print(Solution().reverseString2("hello"))