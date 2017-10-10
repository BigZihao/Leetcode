## citation = [3, 0, 6, 1, 5]


## counting sort 

##H-index is at most the number of papers, which is len(citations) . keep a list of length len(citations)+1, and at each index i, record the number of papers with citations exactly i (except for the last index, which records number of papers with citations >= i). After constructing such list, scan the list from the back, maintain the sum of all encountered number. The sum means how many paper with citation >= the index. If sum>= index, then the index is the h-index.

def hIndex(self, citations):
    stat = [0]*(len(citations)+1)
    for i in citations:
        if i>len(citations):
            i = len(citations)
        stat[i] += 1
    
    sum = 0 
    for j in xrange(len(citations), -1, -1):
        sum += stat[j]
        if sum >= j:
            return j
    return 0


## time: O(nlogn)   spending on sort
## space: O(1)
def hIndex(self, citations):
	citations.sort()
	n = len(citations)
	for i in range(n):
		if citations[i] > (n-i):
			return n - i
	return 0


## time: O(nlogn)
## space: O(n)
def hIndex(self, citations):
	return sum(i<j for i, j in enumerate(sorted(citations, reverse = True)))

#	i 0, 1, 2, 3, 4
#	j 6, 5, 3, 1, 0