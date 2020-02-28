#### Note: This solution only gets 13/15 on the j5, however if we check the input and output it seems to work
#### Just fine, so I'm not sure what the issue is but This solution should work for most cases

import sys
sys.setrecursionlimit(1500) # Default 997

PREVIOUS_STATES = []

class Case:

	def __init__(self, number, order):
		self.number = number
		self.order = order
		
class Node:
    def __init__(self, case, parent):
        self.parent = parent
        self.case = case
        self.children = []



def deepCopy(myList):
	new = []
	for i in range(len(myList)):
		new.append(myList[i][:])
	return new

def ascendingOrder(order):
	for i in range(len(order)):
		if(order[i]):
			if(i + 1 != order[i][0] or len(order[i]) != 1):
				return False
	return True

def getPermutations(order):
	permutations = []
	for i in range(len(order)):
		if(order[i]):
			if(i != len(order) - 1):
				if(not order[i + 1] or order[i][0] < order[i + 1][0]):
					permutation = deepCopy(order)

					permutation[i + 1].insert(0, permutation[i][0])
					permutation[i].remove(permutation[i][0])
					permutations.append(permutation)


			if(i != 0):
				if(not order[i - 1] or order[i][0] < order[i - 1][0]):
					permutation = deepCopy(order)

					permutation[i - 1].insert(0, permutation[i][0])
					permutation[i].remove(permutation[i][0])
					permutations.append(permutation)

			
	return permutations

def possible(order, depth = 0, queue = None):
	if(queue == None):
		queue = []
		queue.append([0, order])
	if(ascendingOrder(order)):
		return depth

	PREVIOUS_STATES.append(order)

	
	permutations = getPermutations(order)

	for permutation in permutations:
		if(not permutation in PREVIOUS_STATES):
			queue.append([depth, permutation])
	queue.remove(queue[0])
	if(len(queue) == 0):
		return False

	check = possible(queue[0][1], queue[0][0] + 1, queue)
	if(check):
		pass
	return check


while True:
	numberOfCoins = int(input())
	# Break out of loop if number is 0
	if(not numberOfCoins):
		break
	orderOfCoins = input().split()
	orderOfCoins = [[int(i)] for i in orderOfCoins] # Convert strings in list to integers

	case = Case(numberOfCoins, orderOfCoins)
	if(ascendingOrder(case.order)):
		PREVIOUS_STATES = []
		print(0)
		continue
	check = possible(case.order)
	if(check):
		print(check) 
	else:
		print("IMPOSSIBLE")
	PREVIOUS_STATES = []