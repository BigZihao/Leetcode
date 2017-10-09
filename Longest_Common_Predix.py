
def longestCommonPrefix(self, strs):
	if not strs:
		return ""

	for i, letter_group in enumerate(zip(*strs)):
		if len(set(letter_group))>1:
			return strs[0][:i]
	else:
		return min(strs, key = len)





def longestCommonPrefix(self, strs):
	sz, ret = zip(*strs), ""
	for c in sz:
		if len(set(c)) > 1: break
		ret+=c[0]
	return ret