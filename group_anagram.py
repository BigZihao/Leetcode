class Solution(object):
	def groupAnagram(self, strs):
		"""
		"""
		dic = {}
		for s in strs:
			s = ''.join(sorted(s))
			if s in dic:
				dic[s].append(string)
			else:
				dic[s] = [string]
		return [dic[x] for x in dic]

	def groupAnagram(self, strs):
		d = {}
		for w in sorted(strs):
			key = tuple(sorted(w))   ## only tuple can be key type of dictionary
			d[key] = d.get(key, []) + [w]
		return d.values()
