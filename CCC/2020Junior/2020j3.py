xs = []
ys = []
for i in range(int(input())):
    data = list(map(int, input().split(",")))
    xs.append(data[0])
    ys.append(data[1])
bottom = [min(xs) - 1, min(ys) - 1]
top = [max(xs) + 1, max(ys) + 1]
print(str(bottom[0]) + "," + str(bottom[1]))
print(str(top[0]) + "," + str(top[1]))