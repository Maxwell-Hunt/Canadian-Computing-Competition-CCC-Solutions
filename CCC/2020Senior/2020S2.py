from math import sqrt

class Cell:
    def __init__(self, value):
        self.value = value
        self.visited = False


numRows = int(input())
numCols = int(input())
grid = []
for i in range(numRows):
    grid.append([Cell(value) for value in list(map(int, input().split()))])

def getFactors(x):
    factors = []
    for i in range(1, int(sqrt(x)) + 1):
        if(x % i == 0):
            factors.extend([(int(x / i), i), (i, int(x / i))])
    return factors


memo = {}
queue = [grid[0][0]]
exited = False
while queue:
    if(grid[numRows - 1][numCols - 1] in queue):
        exited = True
        break
    if(not queue[0].visited):
        factors = None
        if(str(queue[0].value) in memo):
            factors = memo[str(queue[0].value)]
        else:
            factors = getFactors(queue[0].value)
            memo[str(queue[0].value)] = factors
        for factor in factors:
            if(factor[0] <= numRows and factor[1] <= numCols):
                queue.append(grid[factor[0] - 1][factor[1] - 1])
    queue[0].visited = True
    queue.remove(queue[0])

print("yes" if exited else "no")
