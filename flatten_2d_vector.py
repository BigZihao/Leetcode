class solution():
	def __init__(self, vec2d):
		self.col = 0
		self.row = 0
		self.vec2d = vec2d

	def next(self):
		result = self.vec2d[self.row][self.col]
		self.col+=1
		return result

	def hasNext(self):
		while self.row < len(self.vec2d):
			if self.col < len(self.vec2d[self.row]):
				return True

			self.col = 0
			self.row+=1

		return False

