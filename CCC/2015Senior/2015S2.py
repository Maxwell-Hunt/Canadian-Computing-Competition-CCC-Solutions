J = int(input())
A = int(input())
jerseys = []
athletes = []
for i in range(J):
    data = input()
    if(data == "S"):
        jerseys.append([i + 1, 1])
    elif(data == "M"):
        jerseys.append([i + 1, 2])
    else:
        jerseys.append([i + 1, 3])
for i in range(A):
    data = input().split()
    data[1] = int(data[1])
    if(data[0] == "S"):
        athletes.append([1, data[1]])
    elif(data[0] == "M"):
        athletes.append([2, data[1]])
    else:
        athletes.append([3, data[1]])

total = 0
for athlete in athletes:
    for jersey in jerseys:
        if(athlete[1] == jersey[0]):
            if(jersey[1] >= athlete[0]):
                total += 1
                jerseys.remove(jersey)
                break
print(total)