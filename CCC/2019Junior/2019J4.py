grid = [
        [1, 2],
        [3, 4]
        ]
sequence = input()
for instruction in sequence:
    if(instruction == "H"):
        grid.reverse()
    else:
        for i in grid:
            i.reverse()

print(grid[0][0],grid[0][1])
print(grid[1][0],grid[1][1])