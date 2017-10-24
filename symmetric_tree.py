class Solution(object):
	## recursion
	def isSymmetric(self, root):
		def isSym(L, R):
			if L and R:
				return L.val == R.val and isSym(L.left, R.right) and isSym(L.right, R.left)
			else:
				return L == R
		return isSym(root, root)

	## Another simple recursive method, checking whether the original tree = reversed tree with a tuple trick.

	def isSymmetric(sefl, root):
		def tuple_tree(root):
			return root and (root.val, tuple_tree(root.left), tuple_tree(root.right))

		def reverse_tree(root):
			if root:
				root.right, root.left = reverse_tree(root.left), reverse_tree(root.right)
			return root
		return tuple_tree(root) == tuple_tree(reverse_tree(root))



	## Non-recursion
	def isSymmetric(self, root):
		if not root:
			return True
		stack = []
		stack.append((root.left, root.right))

		while stack:
			left, right = stack.pop()
			if not left and not right:
				continue
			elif left and rihgt and left.val == right.val:
				stack.append((left.left, right.right))
				stack.append((left.right, right.left))
			else:
				return False

		return True

	def isSymmetric(self, root):
		if not root:
			return True

		dq = collections.deque([(root.left, root.right)])
		while dq:
			node1, node2 = dq.popleft()
			if not node1 and not node2:
				continue
			if not node1 or not node2:
				return False
			if node1.val !=node2.val:
				return False
			dq.append((node1.left, node2.right))
			dq.append((node1.rihgt, node2.left))

		return True
