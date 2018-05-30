class Solution(object):
	def __init__(self, nestedList):
		self.stack = [[nestedList, 0]]

	def next(self):
		self.hasNext()
		nestedList, i = self.stack[-1]
		self.stack[-1][1]+=1
		return nestedList[i].getInteger()

	def hasNext(self):
		s = self.stack
		while s:
			nestedList, i = s[-1]
			if i == len(nestedList):
				s.pop()
			else:
				x = nestedList[i]
				if x.isInteger():
					return True
				s[-1][1]+=1
				s.append([x.getList(), 0])
		return False


class NestedIterator(object):
	def __init__(self, nestedList):
		self.stack = nestedList[::-1]
		
	def next(self):
		return self.stack.pop().getInteger()

	def hasNext(self):
		while self.stack:
			top = self.stack[-1]
			if top.isInteger():
				return True
			self.stack = self.stack[:-1] + top.getList()[::-1]
		return False



if __name__ == '__main__':
	nestedList = [1,[4,[6]]]
	i, v = NestedIterator(nestedList), []
	while i.hasNext(): 
		v.append(i.next())