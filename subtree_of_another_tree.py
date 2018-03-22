class Solution(object):
	## Naive approach, O(|s| * |t|)
	def isMatch(self, s, t):
		if not (s and t):
			return s is t
		return (s.val == t.val and 
			self.isMatch(s.left, t.left) and 
			self.isMatch(s.right, t.right))

	def isSubtree(self, s, t):
		if self.isMatch(s, t): return True
		if not s:
			return False
		return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

### Basically we convert our tree into string representation, then just check whether substring exists in target string.
    def isSubtree2(self, s, t):
    	def convert(p):
    		return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"
    	return convert(t) in convert(s)
