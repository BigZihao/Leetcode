class Solution(object):
	# k+(n-k)*log(k) time
	def findKthLargest1(self, nums, k):
		heap = nums[:k]
		heapq.heapify(heap)
		for num in nums[k:]:
			if num>heap[0]:
				heapq.heapreplace(heap, num)
		return heap[0]

	def findKthLargest2(self, nums, k):
		return heapq.nlargest(k, nums)[k-1]

