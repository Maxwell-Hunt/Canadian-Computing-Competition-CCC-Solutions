numPieces = input()
pieces = list(map(int, input().split()))
memo = {}
for i in range(len(pieces) - 1):
    for j in range(i + 1, len(pieces)):
        s = pieces[i] + pieces[j]
        if(str(s) not in memo):
            memo[str(s)] = 1
        else:
            memo[str(s)] += 1

totals = [memo[item] for item in memo]
x = max(totals)
print(x, totals.count(x))