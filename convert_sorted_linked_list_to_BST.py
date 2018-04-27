class Solution(object):
	def sortedListofBST1(self, head):
		ls = []
		while head:
			ls.append(head.val)
			head = head.next
		return self.helper(ls, 0, len(ls) - 1)

	def helper(self, ls, start, end):
		if start>end:
			return 
		if start == end:
			return TreeNode(ls[start])
		mid = (start+end)/2
		root = TreeNode(ls[mid])
		root.left = self.helper(ls, start, mid - 1)
		root.right = self.helper(ls, mid + 1, end)
		return root

	def sortedListofBST2(self, head):
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.next.val)
        root.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        root.left = self.sortedListToBST(head)
        return root