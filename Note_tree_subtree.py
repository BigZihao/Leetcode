Tree
subtree
需要检查子树结构的题都需要一个 helper 函数，带着两个 root，递归解决。 如果默认没给，就自己写一个。
子树类问题如果出现不连续，或者需要多个子树信息的时候，自定义 SubtreeTuple 是最合适的选择。
subtree size (int);
在 size / count 这种非负情况下，还可以把符号当 flag 用;
subtree min/max (int);
这种递归结构中先处理完 left / right 再来汇总结果的，其实就是 post-order traversal. 
这点在 search 类 dfs 中也很常见，比如安卓解锁，数解锁方式数量的做法。


top-down  preorder
bottom-up   postorder





0. subtree of another tree
1. same tree
2. Symetric tree
3. convert BST to greater tree
4. dimeter of Binary tree
5. binary tree tilt
6. validate BST
7. sum of lest leaves



0. subtree of another tree


def isSubtree(self, s, t):
	if not s:
		return False
	if self.match(s, t):
		return True
	return self.match(s.left, t) or self.match(s.right, t)

def match(self, s, t):
	if not (s and t):
		return s is t
	return (s.val == t.val and self.match(s.left, t.left) and self.match(s.right, t.right))




1. same tree

def isSameTree(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return p == q


2. Symetric tree
## recursion
def isSymmetric(self, root):
	def isSym(L, R):
		if L and R:
			return L.val == R.val and isSym(L.left, R.right) and isSym(L.right, R.left)
		else:
			return L == R
	return isSym(root, root)


3. Convert BST to greater tree
post-order traversal

def postorder(self, root):
	res = []
	self.helper(root, res)
	return res
def helper(self, root, res):
	if root:
		self.helper(root.left, res)
		self.helper(root.right, res)
		res.append(root.val)

def convertBST(self, root):
	def convertBSTHelper(root, cur_sum):
		if not root:
			return cur_sum

		if root.right:
			cur_sum = convertBSTHelper(root.right, cur_sum)

		cur_sum+=root.val
		root.val = cur_sum
		if root.left:
			cur_sum = convertBSTHelper(root.left, cur_sum)
		return cur_sum

	convertBSTHelper(root, 0)
	return root

4. dimeter of binary tree

def DimOfBinaryTree(self, root):
	self.best = 0
	def depth(root):
		if not root:
			return 0
		left = depth(root.left)
		right = depth(root.right)
		self.best = max(self.best, left+right)
		return 1 + max(left, right)
	depth(root)
	return self.best


5. binary tree tilt

def BinaryTreeTilt(self, root):
	self.ans = 0
	def _sum(node):
		if not node: return 0
		left, right = _sum(node.left), _sum(node.right)
		self.ans+=abs(left-right)
		return node.val + left + right
	_sum(root)
	return self.ans

6. validate BST
	def isValidBST2(self, root, lessThan = float('inf'), largerThan = float('-inf')):
		if not root:
			return True
		if root.val <= largerThan or root.val >= lessThan:
			return False 
		return self.isValidBST2(root.left, min(lessThan, root.val), largerThan) and self.isValidBST2(root.right, lessThan, max(root.val, largerThan))


<<<<<<< HEAD

7. sum of left leaves
=======
7. sum of left leafs
>>>>>>> 1c46f0370df20b137bec7e0b611b48fdb5c01a9a

    def sumOfLeftLeaves3(self, root):
        sum = 0
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            sum+=root.left.val
        sum+= self.sumOfLeftLeaves3(root.left) + self.sumOfLeftLeaves3(root.right)
<<<<<<< HEAD
        return sum
=======
        return sum

# or just iterate through the tree using DFS staskc


def sumOFleftLeaves(self, root):
	stack = [root]
	res = 0
	while stack:
		node = stakc.pop()
		if node.left and not node.left.right and not node.left.left:
			res+=node.left.val
		if node.left:
			stack.append(node.left)
		if node.right:
			stack.append(node.right)
    return res
>>>>>>> 1c46f0370df20b137bec7e0b611b48fdb5c01a9a
