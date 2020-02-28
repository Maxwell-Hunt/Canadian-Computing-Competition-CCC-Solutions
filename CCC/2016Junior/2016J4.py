startTime = list(map(int,input().split(":")))
distance = 0
while distance < 120:
   # print(*startTime, distance)
    if(6 <  startTime[0] < 10 or 14 < startTime[0] < 19):
        distance += 0.5
    else:
        distance += 1
    startTime[1] += 1
    if(startTime[1] > 59):
        startTime[1] = 0
        startTime[0] += 1
    if(startTime[0] > 23):
        startTime[0] = 0
startTime = list(map(str, startTime))
if(int(startTime[0]) < 10):
    startTime[0] = "0" + startTime[0]
if(int(startTime[1]) < 10):
    startTime[1] = "0" + startTime[1]
print(startTime[0] + ":" + startTime[1])


