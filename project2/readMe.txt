CSCI 531: Artificial Intelligence
Section 1
Javier Armando Suarez Rivas

			Program 2: 8 Puzzle Sliding Titles

Language: Python
Run: python (name of class.py)

Data Structure/State Representation:
	State.py:
	The state was represented with a python class named State() which includes
	pointer to the parent state (null in case of root) and several variables
	that contain integer and string values to represent the current state of
	the program like g, h, f, and the matrix representation. In other words
	my state consist of a pointer to the parent node, a matrix, and 4 int values.
	Methods:
		-isValid(): Checks is the generated state is a valid one within the
		parameter of our program.
		-isGoal(): Check is the state is equal to the goal state which is hard-coded
		to match "123456780".
		-__hash__(): Overwrites the python class hash to generate a unique hash
		number, which will be the same in case of repeated state.
		-__eq__(): compares if two State() objects are equal based on the actual
		matrix values.
		-__cmp__(): Overwrites the python compare function to the evaluate f value
		of each node, this method is used to determine the order of
		the Priority Queue.

	PRIORITYQueue.py:
	The PriorityQueue class was obtained from an on-line library. It acts as an
	expected PriorityQueue would. This particular one, in difference from the
	default included in the python library, includes a contains() and__getitem__()
	methods that allow me to identify if a certain element is on the queue and
	to compare if the f value of that element is bigger than the one generated
	and replaced it if is. Increasing space efficiency, but having a significant
	impact on performance due to the iteration of the queue locating the item.
			http://aima-python.googlecode.com/svn/trunk/utils.py

	AStarManhathan.py:
	This file contains the necessary methods to generate all possible movements
	form a specific state, calculation its respective heuristic functions
	(based on the Manhattan heuristic) and returning those values to the
	main AStar() function. Which uses a map to keep track of explored states
	and a priority queue to find the solution.
		The print solution function grabs the solution state and iterates all
	the way until the initial state to determine the path and the length a
	the solution from the start node.

	AStarMissplaced.py:
	Same as above, but with the adapted to hold the misplaced titles heuristic.

	hill_climbing.py:
	This file contains the three different hill climbing algorithms implementations,
	which are: steepest, first choice, and random restart.
		-Steepest: In this algorithm we select the node with the smaller heuristic
		value from all possible children as our next node. The process keeps going
		until a plateau or goal is reached.
		-First Choice: the first choice algorithm, which was deterministically
		implemented, selects the first node with a heuristic function smaller than
		the current, without considering all other neighbor nodes.
		-Random Restart: For this implementation, I decided to randomly generate
		20 more moves and re-run the algorithm until a solution is reached.
		Which makes my code complete, since a solution is always reached, but at
		the expense of performance.



Issues encountered:
	Just the usual debugging problems, like infinite loops and arithmetic
	errors in my logic statements.
	Ignorance of python language class implementation for object comparison,
	which was solved with the __hash__() and __eq__() function additions inside
	of the State() class. At first, I tried using a set to keep track of all the
	repeated states, however since my __eq__() method compared to arrays and
	my __cmp__() function compared the values of the f in each state, when two
	states f function are equal, that should match my __eq__() function, which
	in this case was not and the set did not worked properly. I solved by
	keeping track of the repeated states using a map, with the state represented
	as a string as key.

	In python arrays or list are passes by reference, so if x = [1,2] and
	y = [3,4] if we do a x = y, both arrays match to the same address and modifying
	one will also change the other. After spending some time looking for the bug
	I discovered that whenever I was generating my set of possible moves, I was
	actually passing a different array into my up, down, left and right functions.
	So I was never actually generating the expected results until the bug was
	encountered. The solution was to pass a copy of the object each time.

Known bugs:
	At running time the program will display a syntax warning:
		'SyntaxWarning: name 'generatedStates' is used prior to global declaration'
	This does not affect the performance of the program. I am still learning
	about globals in python.
	Some of the special cases come out with no solution even though Wikipedia
	says it should be one. This part was not required for undergrads

Results:
	Please refer to (astar.xlxs) for the complete data set and to (results.docx)
	for the data explained with more detail.

Sample output:
	-AStarManhathan:
	 1 | 3 | 5 |
	 7 | 4 | 8 |
	 0 | 6 | 2 |
	-----> ↓
	 1 | 3 | 5 |
	 0 | 4 | 8 |
	 7 | 6 | 2 |
	-----> ↓
	 1 | 3 | 5 |
	 4 | 0 | 8 |
	 7 | 6 | 2 |
	-----> ↓
	 1 | 3 | 5 |
	 4 | 8 | 0 |
	 7 | 6 | 2 |
	-----> ↓
	 1 | 3 | 5 |
	 4 | 8 | 2 |
	 7 | 6 | 0 |
	-----> ↓
	 1 | 3 | 5 |
	 4 | 8 | 2 |
	 7 | 0 | 6 |
	-----> ↓
	 1 | 3 | 5 |
	 4 | 0 | 2 |
	 7 | 8 | 6 |
	-----> ↓
	 1 | 3 | 5 |
	 4 | 2 | 0 |
	 7 | 8 | 6 |
	-----> ↓
	 1 | 3 | 0 |
	 4 | 2 | 5 |
	 7 | 8 | 6 |
	-----> ↓
	 1 | 0 | 3 |
	 4 | 2 | 5 |
	 7 | 8 | 6 |
	-----> ↓
	 1 | 2 | 3 |
	 4 | 0 | 5 |
	 7 | 8 | 6 |
	-----> ↓
	 1 | 2 | 3 |
	 4 | 5 | 0 |
	 7 | 8 | 6 |
	-----> ↓
	 1 | 2 | 3 |
	 4 | 5 | 6 |
	 7 | 8 | 0 |
	↑↑↑↑↑
	Number of states added to Queue = 41
	Number of trips = 12
	We made it :)

	-AStarMisplaced:
	 2 | 1 | 5 |
	 0 | 4 | 8 |
	 7 | 6 | 3 |
	-----> ↓
	 2 | 1 | 5 |
	 4 | 0 | 8 |
	 7 | 6 | 3 |
	-----> ↓
	 2 | 1 | 5 |
	 4 | 8 | 0 |
	 7 | 6 | 3 |
	-----> ↓
	 2 | 1 | 5 |
	 4 | 8 | 3 |
	 7 | 6 | 0 |
	-----> ↓
	 2 | 1 | 5 |
	 4 | 8 | 3 |
	 7 | 0 | 6 |
	-----> ↓
	 2 | 1 | 5 |
	 4 | 0 | 3 |
	 7 | 8 | 6 |
	-----> ↓
	 2 | 0 | 5 |
	 4 | 1 | 3 |
	 7 | 8 | 6 |
	-----> ↓
	 2 | 5 | 0 |
	 4 | 1 | 3 |
	 7 | 8 | 6 |
	-----> ↓
	 2 | 5 | 3 |
	 4 | 1 | 0 |
	 7 | 8 | 6 |
	-----> ↓
	 2 | 5 | 3 |
	 4 | 1 | 6 |
	 7 | 8 | 0 |
	-----> ↓
	 2 | 5 | 3 |
	 4 | 1 | 6 |
	 7 | 0 | 8 |
	-----> ↓
	 2 | 5 | 3 |
	 4 | 1 | 6 |
	 0 | 7 | 8 |
	-----> ↓
	 2 | 5 | 3 |
	 0 | 1 | 6 |
	 4 | 7 | 8 |
	-----> ↓
	 2 | 5 | 3 |
	 1 | 0 | 6 |
	 4 | 7 | 8 |
	-----> ↓
	 2 | 0 | 3 |
	 1 | 5 | 6 |
	 4 | 7 | 8 |
	-----> ↓
	 0 | 2 | 3 |
	 1 | 5 | 6 |
	 4 | 7 | 8 |
	-----> ↓
	 1 | 2 | 3 |
	 0 | 5 | 6 |
	 4 | 7 | 8 |
	-----> ↓
	 1 | 2 | 3 |
	 4 | 5 | 6 |
	 0 | 7 | 8 |
	-----> ↓
	 1 | 2 | 3 |
	 4 | 5 | 6 |
	 7 | 0 | 8 |
	-----> ↓
	 1 | 2 | 3 |
	 4 | 5 | 6 |
	 7 | 8 | 0 |
	↑↑↑↑↑
	Number of states added to Queue = 4007
	Number of trips = 19
	We made it :)

	-Hill_Climbing:
	hc_Steepest
	Local Maxima
	 4 | 1 | 2 |
	 7 | 6 | 3 |
	 5 | 8 | 0 |
	3
	7.2e-05
	hc_FirstChoice
	Local Maxima
	 4 | 1 | 2 |
	 7 | 6 | 3 |
	 5 | 8 | 0 |
	3
	hc_RandomRestart
	Goal
	 1 | 2 | 3 |
	 4 | 5 | 6 |
	 7 | 8 | 0 |
	315
