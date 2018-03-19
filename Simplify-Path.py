class Solution(object):
	def simplifyPath(self, path):
		places = [p for p in path.split("/") if p!="." and p!=""]
		stack = []
		for p in places:
			if p == "..":
				if stack:
					stack.pop()
			else:
				stack.append(p)
		return "/" + "/".join(stack)