class State(object):

	def __init__(self, matrix, depth = 0, parent = None, h=0, g=0):
		self.parent = parent
		self.g = g
		self.h = h
		self.matrix = map(int, list(matrix))
		self.depth = depth


	def __eq__(self, other):
		if isinstance(other, State):
			return self.matrix == other.matrix

	def __hash__(self):
		return hash(tuple(self.matrix))

	def __str__(self):
		print = ''
		for i, j in enumerate(self.matrix):
			print += '{0:^3}|'.format(j)
			if i == 2 or i == 5:
				print += '\n'
		return print
	def isGoal(self):
		goalStr = "123456780"
		goal = map(int, list(goalStr))
		if self.matrix == goal:
			return True
		else:
			return False
