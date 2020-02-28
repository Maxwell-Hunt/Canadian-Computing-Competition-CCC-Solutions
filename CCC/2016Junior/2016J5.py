question = int(input())
numBikes = int(input())
peopleA = list(map(int, input().split()))
peopleB = list(map(int, input().split()))
peopleA.sort()
peopleB.sort(reverse = (question - 1))
total = 0
for i in range(len(peopleA)):
    total += max(peopleA[i], peopleB[i])
print(total)
