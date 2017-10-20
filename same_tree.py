class Solution(object):
	## BFS with queue
	def isSameTree1(self, p, q):
		queue = [(p, q)]
		while queue:
			node1, node2 = queue.pop(0)
			if not node1 and not node2:
				continue
			elif None in [node1, node2]:
				return False
			else:
				if node1.val != node2.val:
					return False
				queue.append((node1.left, node2.left))
				queue.append((node1.right, node2.right))
		return True 


    ## DFS with stack
	def isSameTree2(self, p, q):
		stack = [(p, q)]
		while stack:
			node1, node2 = stack.pop()
			if not node1 and not node2:
				continue
			elif None in [node1, node2]:
				return False
			else:
				if node1.val!=node2.val:
					return False
				stack.append((node1.left, node2.left))
				stack.append((node1.right, node2.right))
		return True
