from heapq import heappush, heappop

class Solution(object):

# Time:  O(k * log(min(n, m, k))), where n is the size of num1, and m is the size of num2.
# Space: O(min(n, m, k))


	def kSmallestPairs(self, num1, num2, k):
		queue = []
		def push(i, j):
			if i < len(nums1) and j < len(nums2):
				heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
		push(0, 0)
		pairs = []
		while queue and len(pairs) < k:
			_, i, j = heapq.heappop(queue)
			pairs.append([nums1[i], nums2[j]])
			push(i, j+1)
			if j == 0:
				push(i+1, 0)
		return pairs

	## brute force
	def kSmallestPairs2(self, nums1, nums2, k):
		return map(list, sorted(itertools.product(nums1, nums2), key = sum)[:k])

	## using heap this way saved space, but time is O(m*n),
	## it didn;t use information that the two list are sorted
	def kSmallestPairs3(self, nums1, nums2, k):
		return heapq.nsmallest(k, ([u, v] for u in nums1 for v in nums2), key = sum)

