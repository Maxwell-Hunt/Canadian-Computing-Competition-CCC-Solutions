neighbours = []
location = [0, 0]
for i in range(int(input())):
    neighbours.append(list(map(int, input().split())))
def getMaxDist(location, md, neighbours):
    maxDist = 0
    coords = [0, 0]
    for n in neighbours:
        if(n != location):
            d = (n[0] - location[0])**2 + (n[1] - location[1])**2
            if(md > d > maxDist):
                maxDist = d
                coords = n
    return maxDist, n

treats = 0
data = getMaxDist(location, 10000, neighbours)
while data[0] != 0:
    treats += 1
    dist = data[0]
    newLocation = data[1]
    print(location, newLocation)
    data = getMaxDist(newLocation, dist, neighbours)
    location = newLocation
print(treats)