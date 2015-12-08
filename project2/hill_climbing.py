from State import State
from AStarManhathan import up, down, left, right, createMoves, manhathanDistance
from copy import copy
from random import randint
import time

def createStatesManhatan(current_state):
	children = []
	zeroPosition = current_state.zeroIndex()
	mtrx = current_state.getMatrix()
	# Up
	newArray = up(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.f = manhathanDistance(newArray)
		children.append(newState)
	# Down
	newArray = down(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.f = manhathanDistance(newArray)
		children.append(newState)
	# Left
	newArray = left(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState = State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.f = manhathanDistance(newArray)
		children.append(newState)
	# Right
	newArray = right(current_state.getMatrix(), zeroPosition)
	if newArray is not None:
		newState =	 State(newArray, depth = current_state.depth +1, parent = current_state)
		newState.f = manhathanDistance(newArray)
		children.append(newState)

	return children

def hc_Steepest(matrix):
	# Set up inital condition.
	currentState = State(matrix)
	currentState.f = manhathanDistance(matrix)
	nextState = State(matrix)
	nextState.f = copy(currentState.f)
	statesCount = 1

	while True:
		children = createStatesManhatan(currentState)
		for child in children:
			statesCount +=1
			if child.f < nextState.f:
				nextState = child
		if nextState.f >= currentState.f:
			if nextState.isGoal():
				return "Goal", nextState, statesCount
			else:
				return 'Local Maxima', nextState, statesCount
		currentState = copy(nextState)
	return None

def hc_FirstChoice(matrix):
	# Set up inital condition.
	currentState = State(copy(matrix))
	currentState.f = manhathanDistance(matrix)
	nextState = State(copy(matrix))
	nextState.f = copy(currentState.f)
	statesCount = 1

	while True:
		children = createStatesManhatan(currentState)
		for child in children:
			statesCount +=1
			if child.f < nextState.f:
				nextState = child
				break
		if nextState.f >= currentState.f:
			if nextState.isGoal():
				return "Goal", nextState, statesCount
			else:
				return 'Local Maxima', nextState, statesCount
		currentState = copy(nextState)
	return None

def hc_RandomRestart(matrix, count):
	# Set up inital condition.
	# Ask for all requiered input.
	currentState = State(copy(matrix))
	currentState.f = manhathanDistance(copy(matrix))
	nextState = State(copy(matrix))
	nextState.f = copy(currentState.f)
	statesCount = count

	while True:
		children = createStatesManhatan(currentState)
		for child in children:
			statesCount +=1
			if child.f < nextState.f:
				nextState = child
		if nextState.f >= currentState.f:
			if nextState.isGoal():
				return "Goal", nextState, statesCount
			else:
				return hc_RandomRestart(createMovesRandomRestart(copy(matrix)), statesCount)
		currentState = copy(nextState)
	return None
def createMovesRandomRestart(matrix):
	for i in range(10):
		rand = randint(1, 4)
		if rand == 1:
			up(matrix, matrix.index(0))
		elif rand == 2:
			down(matrix, matrix.index(0))
		elif rand == 3:
			left(matrix, matrix.index(0))
		else:
			right(matrix, matrix.index(0))
	return matrix

def printSolutionHillClimbing(matrix):
	mainSolution =[]
	start = time.clock()
	solution = hc_Steepest(copy(matrix))
	end = time.clock()
	if solution is not None:
		mainSolution.extend(solution)
		mainSolution.append(end-start)
		print "hc_Steepest"
		print solution[0]
		print solution[1]
		print solution[2]
		print end-start
	else:
		print 'No solution'
	start = time.clock()
	solution = hc_FirstChoice(copy(matrix))
	end = time.clock()
	if solution is not None:
		mainSolution.extend(solution)
		mainSolution.append(end-start)
		print "hc_FirstChoice"
		print solution[0]
		print solution[1]
		print solution[2]
	else:
		print 'No solution'
	start = time.clock()
	solution = hc_RandomRestart(copy(matrix), 0)
	end = time.clock()
	if solution is not None:
		print "hc_RandomRestart"
		mainSolution.extend(solution)
		mainSolution.append(end-start)
		print solution[0]
		print solution[1]
		print solution[2]
	else:
		print 'No solution'
	return mainSolution

def main():
	printSolutionHillClimbing(createMoves(map(int, list("123456780"))))


if __name__ == '__main__':
  main()
