class Solution(obejct):
	def findRadius(self, houses, heaters):
		heaters.sort()
		return max(min(abs(house - heaters)
			for i in [bisect.bisect(heaters, house)]
			for heaters in heaters[i-(i>0):i+1])
		for house in houses)

    ## The idea is that for every house, you want to find the closest 2 heaters, and whichever in the 2 that is closer should warm this house. Iterate through the houses, use binary search to find the closest 2 heaters, update answer
	def findRadius(self, houses, heaters):
		heaters.sort()
		ans = 0
		for h in houses:
			hi = bisect.bisect_left(heaters, h)
			left = heaters[hi-1] if hi-1 >= 0 else float('-inf')
			right = heaters[hi] if hi< len(heaters) else float('inf')
			ans = max(ans, min(h-left, right-h))
		return ans

	def findRadius(self, houses, heaters):
		heaters = sorted(heaters) + [float('inf')]
		i=r=0
		for x in sorted(houses):
			while x>=sum(heaters[i:i+2])/2.:
				i+=1
			r = max(r, abs(heaters[i]-x))
		return r