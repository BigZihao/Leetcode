class Solution(object):
	def LengthOfLongestSubstring(self, s):
		start = maxLength = 0
		usedChar = {}

		## loop over
		for i, c in enumerate(s):
			if c in usedChar and start <= usedChar[c]:
				start = usedChar[c] + 1
				# once found, update the pointer of start
			else:
				maxLength = max(maxLength, i - start + 1)
			usedChar[c] = i

		return maxLength


	def LenthOfLongestSubstring2(self, s):
		dic, res, start,  = {}, 0, 0
		for i, ch in enumerate(s):
			if ch in dic:
				# update the res
				res = max(start, dic[ch] + 1)
			dic[ch] = i

		# return should consider the last
		# non-repeated substring
		return max(res, len(s) - start)

if __name__ == "__main__":
	assert Solution().LengthOfLongestSubstring('bbbbbbbb')==1
