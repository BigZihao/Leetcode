#Top K Frequent Elements


## sorting is O(nlogn)
## sorting the whole dictionary, it is actually unnecessary

def topKFrequent(self, nums, k):
	new_dict = dict()
	for item in nums:
		if not new_dict.has_key(item):
			new_dict[item] = 1
		else:
			new_dict[item]+=1
	sorted_dict = sorted(new_dict, key = new_dict.get, reverse= True)
	return sorted_dict[:k]



## heap queue

## time complexity is O(n*log(k))
## use the collections and heapq
import collections
def topKFrequent(self, nums, k):
	num_count = collections.Counter(nums)
	return heapq.nlargest(k, num_count, num_count.get)

