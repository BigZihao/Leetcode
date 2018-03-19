class Solution(object):
	## Solution 1: Reversed first half == Second half?

	## Phase 1: Reverse the first half while finding the middle.
	## Phase 2: Compare the reversed first half with the second half.
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

