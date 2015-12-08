CSCI 531: Artificial Intelligence
Section 1
Javier Armando Suarez Rivas

			Program 1: Cannibals and Missionaries

Language: Python
Compiler: python 523p1.py

Data Structure/State Representation:
		State():
		The state was represented with a python class named State() which includes
		pointer to the parent state (null in case of root) and several variables
		that contain integer and string values to represent the current state of
		the program.
		Methods:
			-isValid(): Checks is the generated state is a valid one within the
									parameter of our program.
			-isGoal(): Check is the state is equal to the goal state.
			-__hash__(): Overwrites the python class hash to generate a unique hash
									 number, which will be the same in case of repeated state.
			-__eq__(): compares if two State() objects are equal based on the actual
								 values.

		FIFOQueue:
		The FIFOQueue class was obtained from an online library. It acts as an
		expected FIFOQueue would.
				http://aima-python.googlecode.com/svn/trunk/utils.py

		createStates():
		This function generates all the possible states based on the position of
		the boat and the number of seats on the boat. It checks if the state
		is valid, and adds the state into and array of States (which is latter
		returned by the function), sets the parent node and adds both into the
		Graph with an edge between both. It increments the total state count
		each time a new state is created.

		bfs():
		Implemented following the pseudo-code provided in class with minor
		modifications. The explored states are added into a python set(), which is a
		data structure that only accepts no repeated items and has an easy check
		for membership. Before each iteration of the while loop, it checks if
		the number of generated states is more than the limit and terminates the
		program if true.

		printSolution():
		This function gets the goal state and loops all the parents until reaching
		the initialState, all states are appended into an array and printed
		afterwards.

Issues encountered:
		Just the usual debugging problems, like infinite loops and arithmetic
		errors in my logic statements.
		Ignorance of python language class implementation for object comparison,
		which was solved with the __hash__() and __eq__() function additions inside
		of the State() class. My elements in the explored set were all being added
		to the set, even if the objects hold the same information.

Known bugs:
	At running time the program will display a syntax warning:
		'SyntaxWarning: name 'generatedStates' is used prior to global declaration'
	This does not affect the performance of the program. I am still learning
	about globals in python.
	Some of the special cases come out with no solution even though Wikipedia
	says it should be one. This part was not required for undergrads

Extra:
	My program generates and displays a graph of the generated States and the
	connection with parent and sons states.

Sample Runs:
	1:
		Enter cannibals and Missionaries separated by commas (3,3):
		3,3
		Enter number of seats on the boat: 2
		Enter Limit num of generatedStates: 1000
		Missionaries and Cannibals solution:
		(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)
		(3,3,left,0,0)
		(2,2,rigth,1,1)
		(2,3,left,1,0)
		(0,3,rigth,3,0)
		(1,3,left,2,0)
		(1,1,rigth,2,2)
		(2,2,left,1,1)
		(2,0,rigth,1,3)
		(3,0,left,0,3)
		(1,0,rigth,2,3)
		(2,0,left,1,3)
		(0,0,rigth,3,3)
		Number of trips = 11
		Number of nodes generated: 106

	2:
		Enter cannibals and Missionaries separated by commas (3,3):
		10,10
		Enter number of seats on the boat: 4
		Enter Limit num of generatedStates: 1000
		States Limit reached.
	3:
		Enter cannibals and Missionaries separated by commas (3,3):
		10,10
		Enter number of seats on the boat: 4
		Enter Limit num of generatedStates: 1000
		States Limit reached.

	4:
		Enter cannibals and Missionaries separated by commas (3,3):
		1,4
		Enter number of seats on the boat: 2
		Enter Limit num of generatedStates: 1000
		Missionaries and Cannibals solution:
		(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)
		(1,4,left,0,0)
		(1,2,rigth,0,2)
		(1,3,left,0,1)
		(1,1,rigth,0,3)
		(1,2,left,0,2)
		(1,0,rigth,0,4)
		(1,1,left,0,3)
		(0,0,rigth,1,4)
		Number of trips = 7
		Number of nodes generated: 176

	5:
		Enter cannibals and Missionaries separated by commas (3,3):
		6,6
		Enter number of seats on the boat: 4
		Enter Limit num of generatedStates: 10000
		Missionaries and Cannibals solution:
		(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)
		(6,6,left,0,0)
		(4,4,rigth,2,2)
		(4,6,left,2,0)
		(0,6,rigth,6,0)
		(2,6,left,4,0)
		(2,2,rigth,4,4)
		(4,4,left,2,2)
		(4,0,rigth,2,6)
		(5,0,left,1,6)
		(1,0,rigth,5,6)
		(2,0,left,4,6)
		(0,0,rigth,6,6)
		Number of trips = 11
		Number of nodes generated: 1721
	6:
		** According to wikipedia, with 3 in the boat 5 couples could cross **
		** The number of generated states is decreased so that the cannibals
		** On the boat are always equal or less than the Missionaries       **
		Enter cannibals and Missionaries separated by commas (3,3):
		5,5
		Enter number of seats on the boat: 3
		Enter Limit num of generatedStates: 1000
		Missionaries and Cannibals solution:
		(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)
		No solution.
		Number of nodes generated: 176
