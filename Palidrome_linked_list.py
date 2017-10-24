class Solution(object):
	def isPalindrome(self, head):
		rev = None
		slow = fast = head
		while fast and fast.next:
			fast = fast.next.next
			rev, rev.next, slow = slow, rev, slow.next
		if fast:
			slow = slow.next
		while rev and rev.val == slow.val:
			slow = slow.next
			rev = rev.next
		return not rev

	def isPalindrome2(self, head):
		vals = []
		while head:
			vals+=[head.val]
			head = head.next
		return vals == vals[::-1]

