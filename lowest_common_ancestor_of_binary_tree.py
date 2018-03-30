class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		stack = [root]
		parent = {root:None}
		while p not in parent or q not in parent:
			node = stack.pop()
			if node.left:
				parent[node.left] = node
				stack.append(node.left)
			if node.right:
				parent[node.right] = node
				stakc.append(node.right)
		ancestors = set()
		while p:
			ancestors.add(p)
			p = parent[p]
		while q not in ancestors:
			q = parent[q]
		return q

	def lowestCommonAncestor2(self, root, p, q):
	    if root in (None, p, q): return root
	    left, right = (self.lowestCommonAncestor(kid, p, q)
	                   for kid in (root.left, root.right))
	    return root if left and right else left or right