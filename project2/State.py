from copy import copy

class State(object):

	def __init__(self, matrix, depth = 0, parent = None, h=0, g=0):
		self.parent = parent
		self.g = g
		self.h = h
		self.matrix = map(int, list(matrix))
		self.depth = depth
		self.f = 0

	def __eq__(self, other):
		if isinstance(other, State):
			return self.matrix == other.matrix
	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash(int(self.to_string()))

	def __cmp__(self, other):
		if self.__eq__(other):
			return 0
		elif self.f > other.f:
			return 1
		elif self.f < other.f:
			return -1
		else:
			return 0
		#return cmp(self.f, other.f)
	def __repr__(self):
		return self.__str__()
	def __str__(self):
		toPrint = ''
		for i, j in enumerate(self.matrix):
			toPrint += '{0:^3}|'.format(j)
			if i == 2 or i == 5:
				toPrint += '\n'
		return toPrint
	def to_string(self):
		return ''.join(map(str, self.matrix))

	def isGoal(self):
		goalStr = "123456780"
		goal = map(int, list(goalStr))
		if self.matrix == goal:
			return True
		else:
			return False
	def zeroIndex(self):
		return copy(self.matrix.index(0))
	def getF(self):
		return self.h + self.g
	def getMatrix(self):
		return copy(self.matrix)
