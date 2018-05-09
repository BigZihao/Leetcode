LCA 类问题是二叉树的高频问题之一；
有只给 root 的；
还有不给 root 给 parent pointer 的。
想面 FB，最好把各种二叉树问题的 recursion / iteration 还有 root / parent pointer 的写法都练熟才行，只 AC 是不够的。



1. LCA of BST
2. LCA of binary tree




1. LCA of BST
	## iteration
def lowestCommonAncestor(self, root, p, q):
	while root:
		if root.val > p.val and root.val > q.val:
			root = root.left
		elif root.val < p.val and root.val < q.val:
			root = root.right
		else:
			return root



2. LCA of binary tree

DFS + stack

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




def lowestCommonAncestor(self, root, p, q):
    
## edge condition
    if root is None:
        return root

    if root == p or root == q:
        return root

## divide
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)


## conquer 
    if left is not None and right is not None:
        return root
    elif left is not None:
        return left
    elif right is not None:
        return right
