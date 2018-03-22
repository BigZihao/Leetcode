class Solution(object):
	def groupAnagram(self, strs):
		"""
		"""
        dic = {}
        for string in strs:
            s = ''.join(sorted(string))
            dic[s] = dic.get(s, []) + [string]
        return [dic[x] for x in dic]

	def groupAnagram(self, strs):
		d = {}
		for w in sorted(strs):
			key = tuple(sorted(w))   ## only tuple can be key type of dictionary
			d[key] = d.get(key, []) + [w]
		return d.values()
