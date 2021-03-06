
## O(n)  O(1)
## iteratively
def mergeTwoLists(self, l1, l2):
	tmp = dummy = ListNode(0)
	## don't know the first node, then set it as dummy, eventually we return dummy.next
	while l1 != None and L2 != None:
		if l1.val < l2.val:
			tmp.next = l1
			l1 = l1.next
		else:
			tmp.next = l2
			l2 = l2.next
		tmp = tmp.next   ## tmp node is keep moving right
    tmp.next = l1 or l2
	return dummy.next



## recursively
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists2(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists2(l1, l2.next)
        return l2


## in-place, iteratively

def mergeTwoLists(self, l1, l2):
    if None in (l1, l2):
        return l1 or l2
    dummy = cur = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = cur.next
            cur.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

## compared with merge array, we can only go right through list

def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    while m > 0 and n > 0:
        if nums[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums2[m-1]
            m-=1
        else:
            nums[m+n-1] = nums2[n-1]
            n-=1
    if n > 0:
        nums1[:n] = nums2[:n]



## if n<m it like insert l2 into l1, then the rest of l1 just stay the place
## if n>m, the rest of l2 has to be in the very begining, since both are already sorted
### merge array is backwards while merge list is forward



def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
