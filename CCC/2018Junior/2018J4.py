N = int(input())
table = []
for i in range(N):
    table.append(list(map(int, input().split())))

def transpose(t):
    new = []
    for i in range(len(t)):
        new.append([])
        for j in range(len(t[i])):
            new[i].append(t[j][i])
    return new

def rotate(t):
    new = transpose(t)
    for row in new:
        row.reverse()
    return new

def increasing(arr):
    for i in range(1, len(arr)):
        if(arr[i] <= arr[i - 1]):
            return False
    return True

def inOrderLeftRight(t):
    for row in t:
        if(not increasing(row)):
            return False
    return True

def inOrderTopBottom(t):
    new = rotate(t)
    for row in new:
        row.reverse()
    if(inOrderLeftRight(new)):
        return True
    return False

while(not inOrderLeftRight(table) or not inOrderTopBottom(table)):
    table = rotate(table)

for row in table:
    print(*row)

