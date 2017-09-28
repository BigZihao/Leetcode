

def mergeTwoLists(self, l1, l2):
	dummy = ListNode(0)
	tmp = dummy
	## don't know the first node, then set it as dummy, eventually we return dummy.next
	while l1 != None and L2 != None:
		if l1.val < l2.val:
			tmp.next = l1
			l1 = l1.next
		else:
			tmp.next = l2
			l2 = l2.next
		tmp = tmp.next   ## tmp node is keep moving right
	if l1 != None:
		tmp.next = l1
	else:
		tmp.next = l2
	return dummy.next