class Solution(object):

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