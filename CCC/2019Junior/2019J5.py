rules = {}
for i in range(3):
    data = input().split()
    rules[data[0]] = data[1]
data = input().split()
numSteps = int(data[0])
initialState = data[1]
finalState = data[2]

def getPermutations(state):
    permutations = []
    for i in range(len(state)):
        ruleIndex = 1
        for rule in rules:
            if(state[i:i+len(rule)] == rule):
                copy = list(state)
                copy[i:i+len(rule)] = list(rules[rule])
                copy = ''.join(copy)
                permutations.append((copy, ruleIndex, i + 1))
            ruleIndex += 1
    return permutations

memo = []
def solve(state, depth = 0, path = None):
    if(depth == numSteps):
        if(state == finalState):
            return path[1:]
        return False

    if(path == None):
        path = [(state, 0, 0)]

    memo.append(state)

    permutations = getPermutations(state)
    for permutation in permutations:
        if(permutation[0] not in memo):
            newPath = path[:]
            newPath.append(permutation)
            x = solve(permutation[0], depth = depth + 1, path = newPath)
        if(x):
            return x
    return False 

solution = solve(initialState)
for step in solution:
    print(step[1], step[2], step[0])