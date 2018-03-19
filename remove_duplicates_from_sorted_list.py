class Solution(object):
	def deleteDuplicates(self, head):
		cur = head
		while cur:
			while cur.next and cur.next.val == cur.val:
				cur.next = cur.next.next
			cur = cur.next
		return head


	## for duplicate you can start with head, for specific value, you need to start with dummy

	def deleteDuplicates(self, head):
		if head and head.next and head.val != head.next.val:
			head.next = self.deleteDuplicates(head.next)
		elif head and head.next:
			head = self.deleteDuplicates(head.next)
		return head