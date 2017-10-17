class Solution(object):
	def numberOfBoomeranges(self, points):
		"""
		:type points: List[List[int]]
		:rtype: int
		"""
		res = 0
		for p in points:
			camp = {}
			for q in points:
				f = p[0] - q[0]
				s = p[1] - q[1]
				camp[f*f + s*s] = 1 + camp.get(f*f + s*s, 0)
			for k in camp:
				res+= camp[k]*(camp[k] - 1)
		return res 


if __name__ == "__main__":
	print(Solution().numberOfBoomeranges([[0,0],[1,0],[2,0]]))