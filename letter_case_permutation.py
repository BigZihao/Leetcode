class Solution(object):
	def letterCasePermutation(self, S):
		res = ['']
		for ch in S:
			if ch.isalpha():
				res = [i+j for i in res for j in [ch.lower(), ch.upper()]]
			else:
				res = [i + ch for i in res]
		return res