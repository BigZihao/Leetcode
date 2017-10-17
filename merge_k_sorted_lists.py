
from Queue import PriorityQueue

class Solution(object):
	def mergeKLists(self, lists):
		dummy = ListNode(None)
		curr = dummy
		q = PriorityQueue()
		for node in lists:
			if node: q.put((node.val, node))
		while q.qsize() > 0:
			curr.next = q.get()[1]
			curr = curr.next
			if curr.next:
				q.put((curr.next.val, curr.next))
		return dummy.next


# By the way, the runtime of this will be O(nklog(k)) for those who are wondering.
# The while loop will run for as many nodes as there are in lists which is order k * n, where n is the length of the list. Each time during the while loop, heappop and heap replace takes O(log(k)) time since we'll have at most k elements in our heap. So the runtime of the while loop is O(nklog(k)).
	def mergeKLists2(self, lists):
		from heapq import heappush, heappop, heapreplace, heapify
		dummy = node = ListNode(0)
		h = [(n.val, n) for n in lists if n]
		heapify(h)
		while h:
			v, n = h[0]
			if n.next is None:
				heappop(h)
			else:
				heapreplace(h, (n.next.val, n.next))
			node.next = next
			node = node.next
		return dummy.next

	# divide and conquer
	def mergeKLists(self, lists):
		if not lists:
			return None

		sentinel = ListNode(0)
		while len(lists) > 1:
			merged = []
			while len(lists) > 1:
				merged.append(self.merge(lists.pop(), lists.pop(), sentinel))
			lists+=merged
		return lists[0]

	def merge(self, x, y, s):
		current = s
		while x and y:
			if x.val < y.val:
				current.next = x
				x = x.next
			else:
				current.next = y
				y = y.next
			current = current.next
		current.next = x if x else y
		return s.next

