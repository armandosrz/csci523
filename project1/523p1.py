import math
import sys


#______________________________________________________________________________
# Queues: FIFOQueue (source: http://aima-python.googlecode.com/svn/trunk/utils.py)

class Queue:
	"""Queue is an abstract class/interface.
	Supports the following methods and functions:
		q.append(item)  -- add an item to the queue
		q.extend(items) -- equivalent to: for item in items: q.append(item)
		q.pop()         -- return the top item from the queue
		len(q)          -- number of items in q (also q.__len())
		item in q       -- does q contain item?
	If Python ever gets interfaces, Queue will be an interface."""

	def __init__(self):
		abstract

	def extend(self, items):
		for item in items: self.append(item)

class FIFOQueue(Queue):
	"""A First-In-First-Out Queue."""
	def __init__(self):
		self.A = []; self.start = 0
	def enqueue(self, item):
		self.A.append(item)
	def __len__(self):
		return len(self.A) - self.start
	def extend(self, items):
		self.A.extend(items)
	def dequeue(self):
		e = self.A[self.start]
		self.start += 1
		if self.start > 5 and self.start > len(self.A)/2:
			self.A = self.A[self.start:]
			self.start = 0
		return e
	def __contains__(self, item):
		return item in self.A[self.start:]

# Program Starts

class State():
	def __init__(self, canLeft, misLeft, ship, canRight, misRight):
		self.canLeft = canLeft
		self.misLeft = misLeft
		self.ship = ship
		self.canRight = canRight
		self.misRight = misRight
		self.parent = None  #Pointer to parent state Generated


	""" The python parser reads logical lines which are terminated when a new
		line is encountered. It is like the ';' in java. Whenever you have a long
		logical line that you want to split in two for readability pourposes
		you can use the backslash character, just like in the function below.
	"""

	def isValid(self):
		if self.misLeft >= 0 and self.misRight >= 0 \
				   and self.canLeft >= 0 and self.canRight >= 0 \
				   and (self.misLeft == 0 or self.misLeft >= self.canLeft) \
				   and (self.misRight == 0 or self.misRight >= self.canRight):
			return True
		else:
			return False

	def isGoal(self):
		if self.misLeft == 0 and self.canLeft == 0:
			return True
		else:
			return False

	def __hash__(self):
		return hash((self.canLeft, self.misLeft, self.ship, self.canRight, self.misRight))

	def __eq__(self, other):
		return (self.canLeft == other.canLeft) and (self.misLeft == other.misLeft)\
					and (self.ship == other.ship) and (self.canRight == other.canRight)\
					and (self.misRight == other.misRight)
	def __str__(self):
		return "(" + str(self.canLeft) + "," + str(self.misLeft) \
						+ "," + self.ship + "," + str(self.canRight) + "," + \
						str(self.misRight) + ")"


def createStates(current_state):

	children = [];
	i = shipCount
	global generatedStates
	generatedSt = generatedStates


	if current_state.ship == 'left':
		# Generate conbinations where the addition of both elements will always be
		# equal to the number of seats on the boat
		for x in xrange(shipCount+1):
			if (i == 0 or i >= x):  # only generate states where c is equal or less than
								  # m on the both
				newState = State(current_state.canLeft-x, current_state.misLeft-i, 'rigth',
								current_state.canRight+x, current_state.misRight+i)
				#print(str(x) + '-' + str(i))
				if newState.isValid():
					#print(newState)
					newState.parent = current_state
					children.append(newState)
				generatedSt += 1
			i = i-1
		# Cannibals to the right with no Missionaries
		for x in xrange(1,shipCount):
			newState = State(current_state.canLeft-x, current_state.misLeft, 'rigth',
							current_state.canRight+x, current_state.misRight)
			#print(str(x))
			if newState.isValid():
				#print(newState)
				newState.parent = current_state
				children.append(newState)
			generatedSt += 1
		# Missionaries to the right with no Cannibals
		for x in xrange(1, shipCount):
			newState = State(current_state.canLeft, current_state.misLeft-x, 'rigth',
							current_state.canRight, current_state.misRight+x)
			#print(str(x))
			if newState.isValid():
				#print(newState)
				newState.parent = current_state
				children.append(newState)
			generatedSt += 1

	else:
		for x in xrange(shipCount+1):
			if (i == 0 or i >= x):
				newState = State(current_state.canLeft+x, current_state.misLeft+i, 'left',
								current_state.canRight-x, current_state.misRight-i)
				if newState.isValid():
					#print('Valid')
					newState.parent = current_state
					children.append(newState)
				generatedSt += 1
			i = i - 1
		for x in xrange(1, shipCount):
			newState = State(current_state.canLeft+x, current_state.misLeft, 'left',
							current_state.canRight-x, current_state.misRight)
			if newState.isValid():
				#print('Valid')
				newState.parent = current_state
				children.append(newState)
			generatedSt += 1
		for x in xrange(1, shipCount):
			newState = State(current_state.canLeft, current_state.misLeft+x, 'left',
							current_state.canRight, current_state.misRight-x)
			if newState.isValid():
				#print('Valid')
				newState.parent = current_state
				children.append(newState)
			generatedSt += 1
	global generatedStates
	generatedStates = generatedSt
	return children

def BFS():
	global shipCount #Capacity of the boat
	global generatedStates #Num of total states Generated.

	# Set up inital condition.
	# Ask for all requiered input.
	print "Enter cannibals and Missionaries separated by commas (3,3): "
	items = [x for x in raw_input().split(',')]
	shipCount = int(raw_input('Enter number of seats on the boat: '))
	generatedStatesLimit = int(raw_input('Enter Limit num of generatedStates: '))
	generatedStates = 1
	initialState = State(int(items[0]),int(items[1]),'left',0, 0)

	if initialState.isGoal():
		return initialState
	frontier = FIFOQueue()
	"""
		A set is an unordered data type with no repited elements.
		It is use for easy comparision of membership
	"""
	explored = set()
	frontier.enqueue(initialState)

	while frontier:
		state = frontier.dequeue()
		explored.add(state)
		children = createStates(state)
		for child in children:
			if (child not in explored) or (child in frontier):
				if child.isGoal():
					return child
				frontier.enqueue(child)
		if generatedStatesLimit < generatedStates:
			print('States Limit reached.')
			sys.exit()
	return None


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
			print "(" + str(state.canLeft) + "," + str(state.misLeft) \
							  + "," + state.ship + "," + str(state.canRight) + "," + \
							  str(state.misRight) + ")"
		print "Number of trips = " + str(pathSize-1)


def main():
	solution = BFS()
	print "Missionaries and Cannibals solution:"
	print "(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)"
	if solution is not None:
		printSolution(solution)
	else:
		print 'No solution.'
	print "Number of nodes generated: " + str(generatedStates)

if __name__ == '__main__':
  main()
