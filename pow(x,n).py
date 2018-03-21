class Solution(object):
	def myPow(self, x, n):
		if n == 0:
			return 1
		if n == -1:
			return 1/x
		return self.myPow(x*x, n/2) * ([1,x][n%2])


		## binary search, recursive solution

	def myPow(self, x, n):
		if n < 0:
			x = 1/x
			n= -n
		res = 1
		while(n>0):
			res*=x if n%2 else 1
			n/=2
			x*=x
		return res
