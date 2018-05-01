class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		stack = [root]
		parent = {root:None}  ##{child:parent}
		## DFS to traverse the tree and find p, q and store their parents
		while p not in parent or q not in parent:
			node = stack.pop()
			if node.left:
				parent[node.left] = node
				stack.append(node.left)
			if node.right:
				parent[node.right] = node
				stack.append(node.right)
		ancestors = set()
		while p:
			ancestors.add(p) # store p's ancestor
			p = parent[p]
		while q not in ancestors:
			q = parent[q]  ## in p's ancestor, find common ancestor that q have
		return q

## recursively
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return root
    
        if root == p or root == q:
            return root
    
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
    
        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        elif right is not None:
            return right


	def lowestCommonAncestor2(self, root, p, q):
	    if root in (None, p, q): return root
	    left, right = (self.lowestCommonAncestor(kid, p, q)
	                   for kid in (root.left, root.right))
	    return root if left and right else left or right