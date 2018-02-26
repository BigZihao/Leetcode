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


log(k) is because of the deepeth of the heap, a new come value might need to bubble down the heap, 
but when n is very large, its actually quite close to O(n)


StefanPochmann 21001  Sep 2, 2016, 12:03 AM
@SLZY Yep, that’s it. Goes through the numbers keeping the so far largest k on a min heap.

I btw went a bit through the history of the module and it looks like nlargest worked like that 
from the start while nsmallest went through several versions and did end up like nlargest 
partially for space reasons. The Python 3 source code also contains some analysis, 
mentions “Other algorithms were not used because they: 1) Took much more auxiliary memory, […]” 
and refers to this comparison showing that it’s not only more space-efficient but on average also 
more time-efficient.

When n is much larger than k, you might think that the O(n + k log n) algorithm is faster 
than the O(n log k) algorithm, but apparently, on average that’s not the case because the O(n log k)
 algorithm is more like O(n). I didn’t read the full analysis, but it makes sense. Let’s say you want 
 the 100 largest of a million random numbers. After a let’s say the first 10000 numbers, 
 the 100 you have in the heap are already pretty large numbers. After all, 
 they’re the largest among those 10000. Any next random number will have a hard time getting 
 into the heap at all, most will get rejected in O(1) because they’re smaller than the heap root. 
 And any number that does make it into the heap makes it even harder for the remaining numbers to get in. 
 If you check this table, you can see the algorithm looks like O(n) on average 
 (when n gets larger and larger compared to k, which is held fixed there while n gets larger and larger).


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