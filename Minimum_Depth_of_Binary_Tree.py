class Solution(object):
## DFS + recrusion
	def minDepth1(self, root):
		if not root:
			return 0
		if None in [root.left, root.right]:
			return max(self.minDepth1(root.left), self.minDepth1(root.right))
		else:
			return min(self.minDepth1(root.left), self.minDepth1(root.right))


## BFS
	def minDepth2(self, root):
		if not root:
			return 0
		queue = collections.deque([(root, 1)])
		while queue:
			node, level = queue.popleft()
			if node:
				if not node.left and not node.right:
					return level
				else:
					queue.append((node.left, level+1))
					queue.append((node.right, level+1))

