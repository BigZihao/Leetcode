

list1 = ["ab","bar","foo"]
list2 = ["bar","foo","de"]


dict = {}
for k in xrange(len(nums)):
	for j in xrange(len(nums[k])):
		dict[nums[k][j]] = dict.get(nums[k][j],0)+1
maxSum = max(dict.values())
sorted([key for key in dict if dict[key]==maxSum])




dict = {}
for k in nums:
	dict[k] = dict.get(k,0)+1

list1= [key+ str(dict[key]) for key in dict]
return ''.join(list1)


def sortRating(l):
	l.sort(key = lambda x:x['rating'], reverse = True)
	return l

sortRating(l)


Merge sorted link list


def mergeTwoLists(self, l1, l2):
	if not l1 or not l2:
		return l1 or l2
	if l1.val < l2.val:
		l1.next = self.mergeTwoLists(l1.next, l2)
		return l1
	else:
		l2.next = self.mergeTwoLists(l2.next,l1)
		return l2



def mergeTwolist(l1,l2):
	result = []
	i = j = 0
	while i < len(l1) and j < len(l2):
		if l1[i]['rating'] < l2[j]['rating']:
			result.append(l1[i])
			i+=1
		else:
			result.append(l2[j])
			j+=1
	result+=l1[i:]
	result+=l2[j:]
	return result

	