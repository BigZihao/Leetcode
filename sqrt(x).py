class Solution(object):

Binary search problem 

	def mySqrt(self, x):
		l, r = 0, x
		while l<=r:
			mid = (l + r)//2
			if mid*mid <=x<(mid+1)*(mid+1):
				return mid
			elif x<mid*mid:
				r = mid
			else:
				l = mid + 1

	def mySqrt(self, x):
		r = x
		while r*r > x:
			r = (r + x/r)/2
		return r


<<<<<<< HEAD

f(x) = S - x^2
X_(n+1) = X_(n) - f(x)/f'(x)
=======
	## binary search idea
	def firstBadVersion(self, n):
		i=1
		j=n
		while i<j:
			k = (i+j)/2
			if isBadVersion(k):
				j=k
			else:
				i=k+1
		return i
>>>>>>> e4ef391033c2de3305cf0e79362db41c634fb7c0
