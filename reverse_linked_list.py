class Solution(object):
	def reverseList(self, head):
		pre, cur = None, head
		while cur:
			cur.next, pre, cur = pre, cur, cur.next
		return pre

	def reverseList(self, head, pre = None):
		if not head: return pre
		cur, head.next = head.next, pre
		return self.reverseList(cur, head)