import math
import sys
from PRIORITYQueue import PriorityQueue
from random import randint
from copy import copy


# Program Starts

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


def createStatesManhatan(current_state):
	children = []
	zeroPosition = current_state.zeroIndex()
	mtrx = current_state.getMatrix()
	# Up
	newArray = up(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = manhathanDistance(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Down
	newArray = down(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = manhathanDistance(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Left
	newArray = left(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = manhathanDistance(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Right
	newArray = right(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = manhathanDistance(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)

	return children


def createStatesMissplaced(current_state):
	children = []
	zeroPosition = current_state.zeroIndex()

	# Up
	newArray = up(current_state.matrix, zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = missplacedTitles(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Down
	newArray = down(current_state.matrix, zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = missplacedTitles(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Left
	newArray = left(current_state.matrix, zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = missplacedTitles(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)
	# Right
	newArray = right(current_state.matrix, zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.h = missplacedTitles(newArray)
		if newState.parent is None:
			newState.g = 0
		else:
			newState.g = newState.parent.g+1
		newState.f = newState.getF()
		children.append(newState)

	return children

def up(matrix, zeroIndex):
	if zeroIndex > 2:
		temp = matrix[zeroIndex]
		matrix[zeroIndex] = matrix[zeroIndex-3]
		matrix[zeroIndex-3] = temp
		return matrix
	else:
		return None

def down(matrix, zeroIndex):
	if zeroIndex < 6:
		temp = matrix[zeroIndex]
		matrix[zeroIndex] = matrix[zeroIndex+3]
		matrix[zeroIndex+3] = temp
		return matrix
	else:
		return None
def right(matrix, zeroIndex):
	#print 'rigth ' + str(zeroIndex) + " " + str(matrix.index(0))
	#print matrix
	if zeroIndex not in [2,5,8]:
		temp = matrix[zeroIndex]
		matrix[zeroIndex] = matrix[zeroIndex+1]
		matrix[zeroIndex+1] = temp
		#print matrix
		return matrix
	else:
		return None
def left(matrix, zeroIndex):
	if zeroIndex not in [0,3,6]:
		temp = matrix[zeroIndex]
		matrix[zeroIndex] = matrix[zeroIndex-1]
		matrix[zeroIndex-1] = temp
		return matrix
	else:
		return None

def missplacedTitles(matrix):
	count = 0
	for i in xrange(len(matrix)):
		if (matrix[i] != i+1 and matrix[i] != 0):
			count += 1
	return count

def manhathanDistance(matrix):
	manhathan = 0
	goal = map(int, list("123456780"))
	for num in matrix:
		if num!=0:
			posMatrix = matrix.index(num)
			yMatrix, xMatrix = divmod(posMatrix, 3)
			posGoal = goal.index(num)
			yGoal, xGoal = divmod(posGoal, 3)
			manhathan += abs(yMatrix - yGoal) + abs(xMatrix - xGoal)
	return manhathan

def createMoves(matrix):
	for i in range(10):
		rand = randint(1,4)
		print str(matrix) + str(rand)
		if rand == 1:
			up(matrix, matrix.index(0))
			print str(matrix) + "up"
		elif rand == 2:
			down(matrix, matrix.index(0))
		elif rand == 3:
			left(matrix, matrix.index(0))
		else:
			right(matrix, matrix.index(0))
	return matrix



def AStar():
	# Set up inital condition.
	# Ask for all requiered input.

	matrix = list("123456780")
	randmatrix = []
	for i in range(len(matrix)):
		index = randint(0, len(matrix)-1)
		randmatrix.append(int(matrix.pop(index)))

	print randmatrix
	matrixWithMoves = createMoves(randmatrix)
	print matrixWithMoves
	initialState = State(matrixWithMoves)
	initialState.f = manhathanDistance(matrixWithMoves)


	if initialState.isGoal():
		return initialState
	frontier = PriorityQueue()
	"""
		A set is an unordered data type with no repited elements.
		It is use for easy comparision of membership
	"""
	explored = {}
	frontier.enqueue(initialState)
	count  = 1
	while frontier:
		"""
		count += 1
		if count == 5:
			break
		"""
		state = frontier.dequeue()
		#print state.to_string() + " " + str(state.f)
		explored[state.to_string()] = 1
		if state.isGoal():
			return state
		children = createStatesManhatan(state)
		for child in children:
			if child.to_string() in explored:
				continue
			if child not in frontier:
				frontier.enqueue(child)
			#elif frontier.__getitem__(child).g > child.g:
			#	continue
			else:
				ch = frontier.__getitem__(child)
				if ch.f > child.f:
					#print child.to_string() + " " + str(ch.f) + " " + str(child.f)
					frontier.__delitem__(child)
					frontier.enqueue(child)
					ts = frontier.__getitem__(child)
			"""

			if (child.to_string() not in explored) and (child not in frontier):
				frontier.enqueue(child)
			elif child.to_string() in explored:
				continue
			elif child in frontier:
				ch = frontier.__getitem__(child)
				if ch.f > child.f:
					#print child.to_string() + " " + str(ch.f) + " " + str(child.f)
					frontier.__delitem__(child)
					frontier.enqueue(child)
					ts = frontier.__getitem__(child)
					#print ts.to_string() + "---" + str(ts.f)
			"""
	"""
	while frontier:
		x = frontier.dequeue()
		print x.to_string() + " " + str(x.f)
	"""
	"""
	for x in explored:
		print x
	return None
	"""

def printSolution(solution):

		path = []
		path.append(solution)
		parent = solution.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		pathSize = len(path)

		for i in range(pathSize):
			state = path[pathSize-i-1]
			print state
			if i < pathSize-1:
				print "-----> " + u"\u2193"
			else:
				print u"\u2191"*5

		print "Number of trips = " + str(pathSize-1)


def main():
	solution = AStar()
	print "A Star using manhathanDistance:"
	if solution is not None:
		printSolution(solution)
		print "We made it :)"
	else:
		print 'No solution.'


if __name__ == '__main__':
  main()
