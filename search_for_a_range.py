class Solution(object):
	def searchRange(self, arr, target):
		start = self.binarySearch(arr, target-0.5)
		if arr[start]!=target:
			return [-1, -1]
		arr.append(0)
		end = self.binarySearch(arr, target+0.5)-1
		return [start, end]



	def binarySearch(self, arr, target):
		start, end = 0, len(arr)-1
		while start<end:
			mid = (start+end)//2
			if target<arr[mid]:
				end = mid
			else:
				start = mid+1
		return start