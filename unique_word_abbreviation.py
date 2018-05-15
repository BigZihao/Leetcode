class solution():
	def __init__(self, dictionary):
		self.dic = {}
		for s in dictionary:
			val = s
			if len(s) > 2:
				s = s[0] + str(len(s) - 2) + s[-1]
			self.dic[s].add(val)

	def isUnique(self, word):
		val = word
		if len(word)>2:
			word = word[0] + str(len(word) -2 ) + word[-1]
		return len(self.dic[word]) == 0 or (len(self.dic[word])==1 and val = list(self.dic[word])[0])