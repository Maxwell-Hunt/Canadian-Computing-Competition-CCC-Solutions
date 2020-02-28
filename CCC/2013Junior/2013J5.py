favouriteTeam = int(input())
gamesPlayed = int(input())
teams = [0, 0, 0, 0]
gamesToBePlayed = ["12","13","14","23","24","34"]
for _ in range(gamesPlayed):
    data = list(map(int, input().split()))
    gamesToBePlayed.remove(str(min(data[0],data[1]))+str(max(data[0],data[1])))
    if(data[2] > data[3]):
        teams[data[0] - 1] += 3
    elif(data[3] > data[2]):
        teams[data[1] - 1] += 3
    else:
        teams[data[0] - 1] += 1
        teams[data[1] - 1] += 1

def greatest(index, myList):
    marker = myList[index]
    for i in range(len(myList)):
        if(i == index):
            continue
        if(myList[i] >= marker):
            return False
    return True

def calculateResults(t, gtbp):
    if(len(gtbp) == 0):
        return t
    newGamesToBePlayed = gtbp[:]
    game = newGamesToBePlayed[0]
    firstVariation = t[:]
    secondVariation = t[:]
    thirdVariation = t[:]
    firstVariation[int(game[0]) - 1] += 3
    secondVariation[int(game[1]) - 1] += 3
    thirdVariation[int(game[0]) - 1] += 1
    thirdVariation[int(game[1]) - 1] += 1
    newGamesToBePlayed.remove(newGamesToBePlayed[0])
    ways = []
    ways.extend(calculateResults(firstVariation,  newGamesToBePlayed))
    ways.extend(calculateResults(secondVariation, newGamesToBePlayed))
    ways.extend(calculateResults(thirdVariation,  newGamesToBePlayed))
    return ways

possibleResultes = calculateResults(teams, gamesToBePlayed)
resultes = []
for i in range(0, len(possibleResultes), 4):
    resultes.append([possibleResultes[i], possibleResultes[i + 1], possibleResultes[i + 2], possibleResultes[i + 3]])
wins = 0
for result in resultes:
    if(greatest(favouriteTeam - 1, result)):
        wins += 1
print(wins)
