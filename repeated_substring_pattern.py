class solutions(object):
	def repeatedStringMatch(self, A, B):
		C = ""
		for i in range(int(len(B)/len(A)) + 3):
			if B in C:
				return i
			C+=A
		return -1