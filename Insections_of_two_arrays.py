class Solution(object):
	def intersection(self, nums1, nums2):
	#sort the two list, and use two pointer to search in the lists to find common elements.
		res = []
		nums1.sort()
		nums2.sort()
		i = j = 0
		while i < len(nums1) and j < len(nums2):
			if nums1[i] < nums2[j]:
				i+=1
			elif nums1[i] > nums2[j]:
				j+=1
			else:
				if nums1[i] not in res:
					res.append(nums1[i])
				i+=1
				j+=1
		return res


if __name__ == "__main__":
	print(Solution().intersection([1,2,3,4,1,2], [1,2,3,2]))