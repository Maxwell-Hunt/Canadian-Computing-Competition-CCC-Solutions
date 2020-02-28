NM = list(map(int,input().split()))
numberOfPeople = NM[0]
people = [[] for i in range(numberOfPeople)]
M = NM[1]
for i in range(M):
    data = list(map(int,input().split()))
    people[data[0] - 1].append(data[1] - 1)
data = input().split()
startingPoint = int(data[0]) - 1
endingPoint = int(data[1]) - 1

queue = [startingPoint]
while queue:
    if(endingPoint in people[queue[0]]):
        print("yes")
        break
    queue.extend(people[queue[0]])
    queue = queue[1:]
else:
    queue = [endingPoint]
    while queue:
        if(startingPoint in people[queue[0]]):
            print("no")
            break
        queue.extend(people[queue[0]])
        queue = queue[1:]
    else:
        print("unknown")