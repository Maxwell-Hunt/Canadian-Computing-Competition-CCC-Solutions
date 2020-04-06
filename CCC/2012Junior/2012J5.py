import time
def ascendingOrder(coins):
	for i in range(1, len(coins)):
		if coins[i]:
			if i + 1 != coins[i][0] or len(coins[i]) != 1:
				return False
		else:
			return False
	return True

def deepcopy(coins):
	new = []
	for coin in coins:
		new.append(coin[:])
	return new

def getPermutations(coins):
	permutations = []
	for i in range(len(coins)):
		if coins[i]:
			if i < len(coins) - 1:
				if not coins[i + 1] or coins[i + 1][0] > coins[i][0]:
					p = deepcopy(coins)
					p[i] = p[i][1:]
					tempPlace = [coins[i][0]]
					tempPlace.extend(coins[i + 1][:])
					p[i + 1] = tempPlace
					permutations.append(p)
			if i > 0:
				if not coins[i - 1] or coins[i - 1][0] > coins[i][0]:
					p = deepcopy(coins)
					p[i] = p[i][1:]
					tempPlace = [coins[i][0]]
					tempPlace.extend(coins[i - 1][:])
					p[i - 1] = tempPlace
					permutations.append(p)
	return permutations

def search(configuration):
	previousStates = []
	queue = [(configuration, 0)]
	while queue:
		if not queue[0][0] in previousStates:
			previousStates.append(queue[0][0])
			if ascendingOrder(queue[0][0]):
				return queue[0][1]
			queue.extend([(p, queue[0][1] + 1) for p in getPermutations(queue[0][0])])
		queue.remove(queue[0])
	return "IMPOSSIBLE"


while True:
	numCoins = int(input())
	if numCoins == 0:
		break
	initialConfiguration = [[int(coin)] for coin in input().split()]
	print(search(initialConfiguration))
