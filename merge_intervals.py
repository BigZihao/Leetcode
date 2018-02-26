class Solution(object):
	def mergeIntervals(self, intervals):
		out = []
		for i in sorted(intervals, key = lambda i: i.start):
			if out and i.start <= out[-1].end:
				out[-1].end = max(out[-1].end, i.end)
			else:
				out+=i,
				#Yes, it has the same effect as that append. 
				#The i, is a tuple (because of the comma), and you can += a tuple to a list.
		return out

	def mergeIntervals2(self, intervals):
		if len(intervals)==0: return []
		intervals = sorted(intervals, key = lambda x: x.start)
		res = [intervals[0]]
		for n in intervals[1:]:
			if n.start <= res[-1].end:
				res[-1].end = max(n.end, res[-1].end)
			else:
				res.append(n)
		return res