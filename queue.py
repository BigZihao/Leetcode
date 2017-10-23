class Queue:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, x):
		self.stack1.append(x)

	def pop(self):
		if len(self.stack2)!=0:
			self.stack2.pop()
		else:
			while len(self.stack1)!=0:
				self.stack2.append(self.stack1.pop())
			self.stack2.pop()

	def peek(self):
		if len(self.stack2)!=0:
			return self.stack2[-1]
		else:
			while len(self.stack1)!=0:
				self.stack2.append(self.stack1.pop())
			return self.stack2[-1]

	def empty(self):
		if len(self.stack1)==0 and len(self.stack2)==0:
			return True
		else:
			return False
