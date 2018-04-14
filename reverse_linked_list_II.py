class Solution(object):
	def reverseBetween(self, head, m, n):
		if m == n:
			return head
		dummy = ListNode(None)
		dummy.next = head
		pre = dummy

		for i in range(m-1):
			pre = pre.next

		reverse = None
		cur = pre.next

		for i in range(n-m+1):
			temp = cur.next
			cur.next = reverse
			reverse = cur
			cur = temp

		pre.next.next = cur
		pre.next = reverse

		return dummy.next