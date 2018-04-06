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
		

	def dfs2(p1,p2):
	    """
	    Two pointers.
	    p1 searches using DFS, Left-Root-Right manner.
	    p2 searches using DFS, Right-Root-Left manner.
	    """
	    # Base case if both nodes are leaves
	    if p1 == None and p2 == None:
	        return True
	    
	    # Recurse if both of them are not null
	    if p1!=None and p2!=None:
	        # values for p1 and p2 must be same.
	        if p1.val != p2.val:
	            return False
	        x = dfs2(p1.left,p2.right)
	        y = dfs2(p1.right,p2.left)
	        # Left of p1 is not same as right of p2 then false.
	        # Simply perform "and" operation on x and y to enforce that. 
	        return x and y
	    
	    # If only one of them is null then return False.
	    return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return dfs2(root.left,root.right)

	## Non-recursion
	## stack DFS
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
