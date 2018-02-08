class Solution(object):
	def swapPairs(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""

		dummy = ListNode(-1)
		dummy.next = head
		prev, cur = dummy, head

		while cur and cur.next:
			nex = cur.next.next
			prev.next = cur.next
			tmp = cur.next.next
			cur.next.next = cur
			cur.next = tmp
			prev = cur 
			cur = nex
		return dummy.next

	def swapPairs(self, head):
		if not head or nor head.next:
			return head

		first, second = head, head.next
		third = second.next
		head = second
		second.next = first
		first.next = self.swapPairs(third)

		return head
