class Solution(object):
	def isHappy(self, n):
		mem = set()
		while n!=1:
			n = sum([int(i) ** 2 for i in str(n)])
			if n in mem:
				return False
			else:
				mem.add(n)
		else:
			return True

	def isHappy2(self, n):
		stop = {1}
		while n not in stop:
			stop.add(n)
			n == sum(int(d)**2 for d in str(n))
		return n == 1




if __name__ == "__main__":
	print(Solution().isHappy(19))