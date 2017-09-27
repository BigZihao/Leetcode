def insertionSortList(self, head):
	cur = dummy = ListNode(0)
	while head:
		if cur and cur.val > head.val:
			cur = dummy
		while cur.next and cur.next.val < head.val:
			cur = cur.next
		cur.next, cur.next.next, head = head, cur.next, head.next
	return dummy.next



def insertionSortList(self, head):
	dummy = ListNode(0)

	while head:
		temp = dummy
		next = head.next 
		while temp.next and temp.next.val < head.val:
			temp = temp.next
		head.next = temp.next
		temp.next = head
		head = next
	return dummy.next