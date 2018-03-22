class solution(object):
	def tree2str(self, t):
		def preorder(root):
			if root is None:
				return ""
			s = str(root.val)
			l = preorder(root.left)
			r = preorder(root.right)
			if r=="" and l == "":
				return s
			elif l == "":
				s+="()" + "(" + r + ")"
			elif r == "":
				s+="(" + l + ")"
			else:
				s+="(" + l +")" + "(" + r + ")"
			return s
		return preorder(t)


	## or lets do this recursively 
#If the tree is empty, we return an empty string.
#We record each child as ‘(’ + (string of child) + ‘)’
#If there is a right child but no left child, we still need to record ‘()’ instead of empty string.
	def tree2str2(self, r):
		if not t: return ''
		left = '({})'.format(self.tree2str2(t.left)) if (t.left or t.right) else ''
		right = '({})'.format(self.tree2str2(t.right)) if t.right else ''
		return '{}{}{}'.format(t.val, left, right)
