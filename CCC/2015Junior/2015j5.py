numPieces = int(input())
numPeople = int(input())
def numWays(pieces, people, minTake = 1, memo = None):
    if memo == None:
        memo = {}
    if(people == 1 or people == pieces):
        return 1
    possibleWays = pieces//people
    total = 0
    for i in range(1, possibleWays+1):
        if(i >= minTake):
            if not (pieces - i, people - 1, i) in memo:
                x = numWays(pieces-i, people-1, minTake = i, memo = memo)
                memo[(pieces - i, people - 1, i)] = x
                total += x
            else:
                total += memo[(pieces - i, people - 1, i)]
    return total

print(numWays(numPieces, numPeople))
