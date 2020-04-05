from math import sqrt

class Cell:
    def __init__(self, value):
        self.value = value
        self.visited = False

rows = int(input())
cols = int(input())
grid = [list(map(Cell,list(map(int, input().split())))) for _ in range(rows)]

queue = [grid[0][0]]
ended = False
while(queue):
    queue[0].visited = True

    factors = []
    for i in range(1, int(sqrt(queue[0].value)) + 1):
        ni = queue[0].value / i
        if(i == rows and ni == cols) or (ni == rows and i == cols):
                ended = True
                break
        if(int(ni) == ni):
            ni = int(ni)
            if(i - 1 < rows and ni - 1 < cols):
                if(not grid[i - 1][ni - 1].visited):
                    factors.append(grid[i - 1][ni - 1])
            if(ni != i):
                if(ni - 1 < rows and i - 1 < cols):
                    if(not grid[ni - 1][i - 1].visited):
                        factors.append(grid[ni - 1][i - 1])
    if(ended):
        break
    queue.extend(factors)
    queue.remove(queue[0])

print("yes" if ended else "no")