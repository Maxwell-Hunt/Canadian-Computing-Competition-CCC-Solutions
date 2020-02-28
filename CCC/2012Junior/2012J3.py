scaleFactor = int(input())
grid = ["*x*",
        " xx",
        "* *"]
for row in grid:
    for i in range(scaleFactor):
        for char in row:
            print(char*scaleFactor, end="")
        print()