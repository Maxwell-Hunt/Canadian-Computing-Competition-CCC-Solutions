from math import sqrt

rows = int(input())
cols = int(input())

grid = [list(map(int, input().split())) for _ in range(rows)]

def getFactors(n):
    factors = []
    step = 1 if n % 2 == 0 else 2
    for i in range(1, int(sqrt(n)) + 1, step):
        if n % i == 0:
            j = int(n / i)
            if j < rows + 1 and i < cols + 1:
                factors.append((j, i))

            if i < rows + 1 and j < cols + 1:
                factors.append((i, j))
    return factors

# Breadth First Search
memo = {}
queue = [grid[0][0]]
goalReached = False
while queue:
    if not queue[0] in memo:
        memo[queue[0]] = 0
        for factor in getFactors(queue[0]):
            if factor == (rows, cols):
                goalReached = True
                break
            queue.append(grid[factor[0] - 1][factor[1] - 1])
        if goalReached:
            break
    queue.remove(queue[0])

print("yes" if goalReached else "no")
