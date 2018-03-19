class Solution(object):
	def reverseStr(self, s, k):
		end = 0
		n = len(s)
		while end< n:
			if n-end<k:
				s = s[:end] + s[end:][::-1]
			else:
				s = s[:end] + s[end:end+k][::-1] + s[end+k:]
			end = end+2*k
		return s

	def reverseStr2(self,s, k):
		s = list(s)
		for i in range(0, len(s), 2*k):
			s[i:i+k] = reversed(s[i:i+k])
		return "".join(s)

	def reverseStr3(self, s, k):
		return s[:k][::-1] + s[k:2*k] + self.reverseStr3(s[2*k:], k) if s else ""