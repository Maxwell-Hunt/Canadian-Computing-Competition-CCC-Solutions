numPeople = int(input())
pairs = {}
orderA = input().split()
orderB = input().split()
for i in range(len(orderA)):
    pairs[orderA[i]] = orderB[i]

for member in pairs:
    if(pairs[member] == member or pairs[pairs[member]] != member):
        print("bad")
        break
else:
    print("good")