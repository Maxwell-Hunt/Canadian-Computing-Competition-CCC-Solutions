numRolls = int(input())
scoreA = 100
scoreB = 100
for _ in range(numRolls):
    roll = list(map(int,input().split(" ")))
    if(roll[0] > roll[1]):
        scoreB -= roll[0]
    elif(roll[1] > roll[0]):
        scoreA -= roll[1]
    else:
        continue
print(scoreA)
print(scoreB)
