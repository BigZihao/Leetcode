
class Solution(object):
	def hasCycle(self, head):
		try:
			slow = head
			fast = head.next
			while slow is not fast:
				slow = slow.next
				fast = fast.next.next
			return True
		except:
			return False

	def hasCycle(self, head):
	    slow = fast = head
	    while fast and fast.next:
	        fast = fast.next.next
	        slow = slow.next
	        if slow == fast:
	            return True
	    return False
