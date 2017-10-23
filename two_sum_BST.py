class Solution(object):
	def findTarget(self, root, k):
		if not root: return False
		bfs, s = [root], set()
		for i in bfs:
			if k - i.val in s: return True
			s.add(i.val)
			if i.left: bfs.append(i.left)
			if i.right: bfs.append(i.right)
		return False



	def findTarget2(self, root, k):
		a = set()
		self.f = False
		def dfs(root, k):
			if not root:
				return
			if root.val not in a:
				a.add(k - root.val)
			else:
				self.f = True
			dfs(root.left, k)
			dfs(root.right, k)
		dfs(root, k)
		return self.f

		## time complexity O(M)
	def findTarget3(self, root, k):
		self.dset = set()
		self.traverse(root)
		for n in self.dset:
			if k - n != n and k - n in self.dset:
				return True
		return False

	def traverse(self, root):
		if not root: return 
		self.dset.add(root.val)
		self.traverse(root.left)
		self.traverse(root.right)