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
	return heapq.nlargest(k, num_count, key = num_count.get)


### well for large dataset, sort the dictionary takes times. heap will be better data structure
## insertion: insert at the bottom and bubble it up 
## the implementation can be just a array instead of node structure

class Heap(object):
	def __init__(self, size):
		self.num = 0
		self.size = 0
		self.value = [None] * size

	def __repr__(self):
		return '<Thing: %s>' % (self.data,)