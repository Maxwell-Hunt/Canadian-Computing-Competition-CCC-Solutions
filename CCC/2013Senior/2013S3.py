teams = [0, 0, 0, 0]
gamesToBePlayed = [
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
    [3, 4]
]
favouriteTeam = int(input()) - 1
gamesPlayed = int(input())
for i in range(gamesPlayed):
    data = list(map(int, input().split()))
    if(data[2] > data[3]):
        teams[data[0] - 1] += 3
    elif(data[2] == data[3]):
        teams[data[0] - 1] += 1
        teams[data[1] - 1] += 1
    else:
        teams[data[1] - 1] += 3
    gamesToBePlayed.remove(data[:2])

def getPermutations(scores, match):
    w = scores[:]
    t = scores[:]
    l = scores[:]
    w[match[0] - 1] += 3
    t[match[0] - 1] += 1
    t[match[1] - 1] += 1
    l[match[1] - 1] += 3
    return [w, t, l]

solution = []
def solve(scores, gamesLeft):
    global solution
    if(not gamesLeft):
        solution.append(scores)
        return None

    permutations = getPermutations(scores, gamesLeft[0])
    for item in permutations:
        solve(item, gamesLeft[1:])

solve(teams, gamesToBePlayed)
totalWins = 0
for outcome in solution:
    m = max(outcome)
    if(outcome[favouriteTeam] == m):
        outcome.remove(m)
        if(m > max(outcome)):
            totalWins += 1
print(totalWins)