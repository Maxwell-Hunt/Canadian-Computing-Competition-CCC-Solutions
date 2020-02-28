weightLimit = int(input())
weights = [int(input()) for i in range(int(input()))]
total = 0
for i in range(len(weights)):
    if(i >= 4):
        total -= weights[i - 4]
    total += weights[i]
    if(total > weightLimit):
        print(i)
        break
else:
    print(len(weights))
