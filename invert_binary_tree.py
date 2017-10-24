class Solution(object):
	def invertTree(self, root):
		if root:
			root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
			return root

	def invertTree2(self, root):
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				node.left, node.right = node.right, node.left
				stack+=node.left, node.right
		return root

	##BFS
	def invertTree3(self, root):
		queue = collections.deque([(root)])
		while queue:
			node = queue.popleft()
			if node:
				node.left, node.right = node.right, node.left
				queue.append(node.left)
				queue.append(node.right)
		return root

    ## DFS
	def invertTree4(self, root):
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				node.left, node.right = node.right, node.left
				stack.extend([node.right, node.left])
		return root

