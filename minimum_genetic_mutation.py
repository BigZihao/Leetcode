class Solution():
	def minMutation(self, start, end, bank):
		bank, v, q = set(bank), {start}, [(start, 0)]
		for g, k in q:
			for s in (g[:i] + cc + g[i+1:] for i, c in enumerate(g) for cc in 'ACGT'):
				if s in bank and s not in v:
					if s == end:
						return k + 1
					q.append((s, k + 1))
					v.add(s)
		return -1 