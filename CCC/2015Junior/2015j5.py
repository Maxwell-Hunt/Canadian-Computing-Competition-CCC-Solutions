numPieces = int(input())
numPeople = int(input())
def numWays(pieces, people, minTake):
    if(people == 1 or people == pieces):
        return 1
    possibleWays = pieces//people
    total = 0
    for i in range(1, possibleWays+1):
        if(i >= minTake):
            total += numWays(pieces-i, people-1, i)
    return total

print(numWays(numPieces, numPeople, 1))
