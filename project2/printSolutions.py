import csv
from copy import copy
import AStarManhathan
import AStarMissplaced
from random import randint
import hill_climbing
import sys
sys.setrecursionlimit(10000)

def main():

	with open("a_star.csv", 'w') as csvf:
		write = csv.writer(csvf)
		write.writerow(['Sate', 'Manhathan States', 'Manhatan Moves','Manhatan time','Missplaced States',\
						'Missplaced Moves','Missplaced time' ,'hc_Steepest Staus: ', 'hc_Steepest: States '\
						,'hc_Steepest time:', 'hc_FirstChoice: Status', 'hc_FirstChoice: states', \
						'hc_FirstChoice Time', 'hc_RandomRestart Status', 'hc_RandomRestart: states'\
						'hc_RandomRestart time'])
		for x in xrange(50):
			matrix = map(int,list("123456780"))
			matrixWithMoves = createMoves(matrix)
			manhathan = AStarManhathan.printSolutionManhatan(copy(matrixWithMoves))
			missplaced = AStarMissplaced.printSolutionMissplaced(copy(matrixWithMoves))
			state = ''.join(map(str, matrixWithMoves))
			hc = hill_climbing.printSolutionHillClimbing(copy(matrixWithMoves))
			write.writerow([state, manhathan[0], manhathan[1],manhathan[2],\
							missplaced[0],missplaced[1], missplaced[2],\
							hc[0], hc[2], hc[3],\
							hc[4], hc[6], hc[7],\
							hc[8], hc[10], hc[11]])



def createMoves(matrix):
	for i in range(100):
		rand = randint(1,4)
		if rand == 1:
			AStarMissplaced.up(matrix, matrix.index(0))
		elif rand == 2:
			AStarMissplaced.down(matrix, matrix.index(0))
		elif rand == 3:
			AStarMissplaced.left(matrix, matrix.index(0))
		else:
			AStarMissplaced.right(matrix, matrix.index(0))
	return matrix

if __name__ == '__main__':
  main()
