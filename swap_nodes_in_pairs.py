class Solution(object):
	def swapPairs(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""

		dummy = p = ListNode(0)
		dummy.next = head
		while head and head.next:
			tmp = head.next
			head.next = tmp.next
			tmp.next = head
			p.next = tmp
			head = head.next
			p = tmp.next
		return dummy.next
    ## recursion

	def swapPairs(self, head):
		if not head or nor head.next:
			return head

		first, second = head, head.next
		third = second.next
		head = second
		second.next = first
		first.next = self.swapPairs(third)

		return head
