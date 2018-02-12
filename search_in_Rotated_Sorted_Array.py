## topic binary search 

## basic case : Sqrt(x)

class Solution(object):

	def myIntSqrt(self, x):
		l, r = 0, x
		while l<r:
			mid = l + (r-l)//2
			if mid*mid <= x < (mid+1)*(mid+1):
				return mid
			elif x < mid*mid:
				r = mid
			else:
				l = mid + 1

	def NewtonMethodforSqrt(self, x, max_iter = 10, precision=0.01):
		x0 = x/2
		for _ in range(max_iter):
			x1 = (x0 + x/x0)/2
			### Xn+1 = Xn - (f(xn)/f'(xn))  newton's method
			if abs(x1 - x0)<precision:
				break
			else:
				x0 = x1
		return x1


	def Search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype Index: int
		"""
		if not nums:
			return -1

		low, high = 0, len(nums)-1
		while low<= high:
			mid = (low + high)//2
			if target == nums[mid]:
				return mid

			if nums[low] <= nums[mid]:
				if nums[low] <= target <= nums[mid]:
					high = mid-1
				else:
					low = mid + 1
			else:
				if nums[mid] <= target <= nums[high]:
					low = mid + 1
				else:
					high = mid - 1

		return -1 

