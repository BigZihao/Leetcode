class Solution(object):
	def isValid(self, s):
		stack = []
		dict = {"}":"{", "]":"[", ")":"("}
		for char in s:
			if char in dict.values():
				stack.append(char)
			elif char in dict.keys():
				if dict[char]!=stack.pop() or stack == []:
					return False
			else:
				return False
		return stack == []

	def isValid2(self, s):
		
if __name__ == "__main__":
	print(Solution().isValid("["))