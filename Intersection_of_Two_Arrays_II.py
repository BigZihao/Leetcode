##Intersection of Two Arrays II


## option 1: using dictionary

def intersect(nums1, nums2):

	counts = {}
	res = []

	for num in nums1:
		counts[num] = counts.get(num, 0) + 1

	for num in nums2:
		if num in counts and counts[num]>0:
			res.append(num)
			counts[num]-=1
	return res


from collections import Counter 


def intersect2(nums1, nums2):
	a, b = map(Counter,(nums1, nums2))
	return list((a & b).elements())


## option 3: using sorted array, the idea is similar to merge in mergesort

def intersect3(nums1, nums2):
	nums1, nums2 = sorted(nums1), sorted(nums2)
	pt1, pt2 = 0, 0 
	res = []
	while True:
		try:
			if nums1[pt1] > nums2[pt2]:
				pt2+= 1
			elif nums1[pt1] < nums2[pt2]:
				pt1+= 1
			else: 
				res.append(nums1[pt1])
				pt1+= 1
				pt2+= 1
		except IndexError:
			break
	return res
	

def intersect4(nums1, nums2):
	dict1 = dict()
	for i in nums1:
		dict[i] = dict.get(i, 0) +1
	ret= []
	for i in nums2:
		if i in dict1 and dict1[i]>0:
			ret.append(i)
			dict1[i]-=1
	return ret





print(intersect3([1,2,2,2,2,1,1,4],[1,2,4,4,5]))