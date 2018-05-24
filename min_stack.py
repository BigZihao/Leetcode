class MinStack(object):
	def __init__(self):
		self.q = []

    ## everytime you add one element, store the mimun the same time
	def push(self, x):
		curMin = self.getMin()
		if curMin == None or x < curMin:
			curMin = x
		self.q.append((x, curMin))

	def pop(self):
		self.q.pop()

	def top(self):
		if len(self.q) == 0:
			return None
		else:
			return self.q[len(self.q) - 1][0]

	def getMin(self):
		if len(self.q) == 0:
			return None
		else:
			return self.q[len(self.q) - 1][1]

if __name__ == "__main__":
	minStack = MinStack();
	minStack.push(-2);
	minStack.push(0);
	minStack.push(-3);
	minStack.getMin();   
	print(minStack.pop());
	print(minStack.top());      
	print(minStack.getMin());   

