class Solution(object):
	def sort(self, alist):
		print("sorting", alist)
		quicksort(alist, 0, len(alist)-1)

	def quicksort(self, alist, left, right):
		if left < right:
			splitpoint = partition(alist, left, right)
			print("sorting", alist[left:(splitpoint-1)])
			self.quicksort(alist, left, splitpoint-1)
			print("sorting", alist[(splitpoint+1):right])
			self.quicksort(alist, splitpoint+1, right)

	def partition(self, alist, left, right):
		pivotvalue = alist[left]

		leftmark = left + 1
		rightmark = right 

		done = False
		while not done:

			while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
				leftmark = leftmark + 1
			while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
				rightmark = rightmark - 1
			if rightmark < leftmark:
				done = True
			else:
				temp = alist[leftmark]
				alist[leftmark] = alist[rightmark]
				alist[rightmark] = temp
		temp = alist[left]
		alist[left] = alist[rightmark]
		alist[rightmark] = temp

		print("splitting at", rightmark)

		return rightmark


	## option 2: generator

	def qsort(self, alist):
		if len(alist)<1:
			pass
		elif len(alist) == 1:
			yield alist[0]
		else:
			yield from self.qsort([x for x in alist if x < alist[0]])
			yield from self.qsort([x for x in alist if x == alist[0]])
			yield from self.qsort([x for x in alist if x > alist[0]])


	def first_n(self, seq, n):
		it = iter(seq)
		return [next(it, None) for _ in range(n)]


	## Option 3 list generator

	def quicksort3(self, alist):
		if len(alist) <= 1:
			return alist
		pivot = alist[len(alist)//2]
		left = [x for x in alist if x < pivot]
		middle = [x for x in alist if x == pivot]
		right = [x for x in alist if x > pivot]
		return self.quicksort3(left) + middle + self.quicksort3(right)


alist = [54,26,93,17,77,31,44,55,20]
if __name__ == "__main__":
	print(Solution().quicksort3(alist))
