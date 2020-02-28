numMinutes = int(input())
numChores = int(input())
choreTimes = []
for _ in range(numChores):
    choreTimes.append(int(input()))

completed = 0
m = min(choreTimes)
while(numMinutes >= m):
    # print(choreTimes, numMinutes, completed)
    # print("*"*10)
    numMinutes -= m
    choreTimes.remove(m)
    completed += 1
    m = min(choreTimes)
print(completed)
