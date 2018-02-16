class Solution(object):
	def __init__(self, head):
		self.head = head


   #  here is actually pretty simple that k = 1
	def getRandom(self):
		result, node, index = self.head, self.head.next, 1
		while node:
			if random.randint(0, index) is 0:
				result = node
			node = node.next
			index+=1
		return result.val

## when i >k
## for new i, selction is k/(i+1)
## old replace k/(i+1)* 1/k = 1/(i+1),,,   old stay = 1 - (1/(i+1)) = i/(i+1)
## k/i * i/(i+1) = k/(i+1)
## so for all items, they are selected by probability k/n

