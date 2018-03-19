import heapq
class Solution(object):
	def topKFrequentWord(self, words, k):
		wc, h = collections.Counter(words), []
		for w, c in wc.items():
			## using the wc.items() will give the alphabetical order
			heapq.heappush(h, (-c, w))
		return [heapq.heappop(h)[1] for _ in range(k)]


	def topKFrequentWord2(self, words, k):
		d = {}
		for word in words:
			d[word] = d.get(word, 0) + 1
		res = sorted(d, key = lambda word: (-d[word], word))
		## sort by both the order of frequency and alphabetical order using the tuple 
		return res[:k]

		
    from heapq import *
	def topFrequentWord3(self, words, k):
		d = {}
		for word in words:
			d[word] = d.get(d, 0)+1
		tu = [(-i, n) for n, i in d.items()]
		h = nsmallest(k, tu)
		return [i[1] for i in h]





