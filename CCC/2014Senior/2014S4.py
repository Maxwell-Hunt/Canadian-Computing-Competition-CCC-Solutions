numWindows = int(input())
tintThreshold = int(input())
tintedArea = 0
windows = []
largestX = 0
largestY = 0
for i in range(numWindows):
    data = list(map(int, input().split()))
    if(data[2] > largestX):
        largestX = data[2]
    if(data[3] > largestY):
        largestY = data[3]
    windows.append(data)

surface = []
for i in range(largestX + 1):
    surface.append([])
    for j in range(largestY + 1):
        surface[i].append(0)

for window in windows:
    for i in range(window[0], window[2]):
        for j in range(window[1], window[3]):
            surface[i][j] += window[4]
            if(surface[i][j] >= tintThreshold):
                tintedArea += 1
                surface[i][j] = -1000000

print(tintedArea)