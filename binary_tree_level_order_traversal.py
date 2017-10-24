class Solution(object):
	## BFS using queue
	def levelOrder6(self, root):
		results = []
		if not root:
			return results
		q = [root]
		while q:
			new_q = []
			results.append([n.val for n in q])
			for node in q:
				if node.left:
					new_q.append(node.left)
				if node.right:
					new_q.append(node.right)
			q = new_q
		return results

## DFS but keep tracking of the level
    def levelOrder7(self, root):
    	stack = [(root, 0)]
    	res = []
    	while stack:
    		node, level = stack.pop()
    		if node:
    			if len(res)< level + 1:
    				res.insert(level, [])
    			res[level].append(node.val)
    			if node.right:
    				stack.append((node.right, level+1))
    			if node.left:
    				stack.append((node.left, level +1))
    	return res






	def levelOrder(self, root):
		ans, level = [], [root]
		while root and level:
			ans.append([node.val for node in level])
			LRpair = [(node.left, node.right) for node in level]
			level = [leaf for LR in LRpair for leaf in LR if leaf]
		return ans

	def levelOrder2(self, root):
		if not root:
			return []
		ans, level = [], [root]
		while level:
			ans.append([node.val for node in level])
			temp = []
			for node in level:
				temp.extend([node.left, node.right])
			level = [leaf for leaf in temp if leaf]
		return ans

	def levelOrder3(self, root):
		if not root: return []
		stack, queue, res, nCount = [root], [], [[root.val]], 1
		while stack:
			temp = stack.pop(0)
			if temp.left:
				stack.append(temp.left)
			if temp.right:
				stack.append(temp.right)
			nCount-=1
			if nCount==0:
				queue = [x.val for x in stack]
				res+=[queue] if queue else []
				nCount = len(stack)
		return res

	def levelOrder4(self, root):
		if root is None: return []
		q = [[root]]
		for level in q:
			record = []
			for node in level:
				if node.left: record.append(node.left)
				if node.right: record.append(node.right)
			if record: q.append(record)
		return [[x.val for x  in level] for level in q]

	def preorder(self, root, level, res):
		if root:
			if len(res) < level+1:
				res.append([])
			res[level].append(root.val)
			self.preorder(root.left, level+1, res)
			self.preorder(root.right, level+1, res)

	def levelOrder5(self, root):
		res= []
		self.preorder(root, 0, res)
		return res



