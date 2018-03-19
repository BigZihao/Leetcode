class Solution(object):
	def removeElements(self, head, val):
		dummy = ListNode(0)
		dummy.next = head
		cur = dummy
		while cur and cur.next:
			if cur.next.val == val:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return dummy.next