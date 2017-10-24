class Solution(obejct):
	def hasPathSum(self, root, sumN):
		if not root:
			return False

		if not root.left and not root.right and root.val == sumN:
			return True

		sumN-=root.val

		return self.hasPathSum(root.left, sumN) or self.hasPathSum(root.right, sumN)


    ## DFS
	def hasPathSum2(self, root, sumN):
		if root is None:
			return False
		stack = [(root, sumN)]
		while stack:
			node, _sum = stack.pop()
			if node.left is node.right is None and node.val == _sum:
				return True
			if node.left:
				stack.append((node.left, _sum - node.val))
			if node.right:
				stack.append((node.right, _sum - node.val))
		return False

    ## BFS
	def hasPathSum3(self, root, sumN):
		if not root:
			return False
		queue = [(root, sumN - root.val)]
		while queue:
			curr, val = queue.pop(0)
			if not curr.left and not curr.right:
				if val == 0:
					return True
			if curr.left:
				queue.append((curr.left, val - curr.left.val))
			if curr.right:
				queue.append((curr.right, val - curr.right.val))
		return False


