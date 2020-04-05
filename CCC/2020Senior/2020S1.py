observations = [list(map(int, input().split())) for _ in range(int(input()))]
observations.sort()
maxSpeed = 0
for i in range(len(observations) - 1):
    o = observations[i]
    o1 = observations[i + 1]
    distance = max(o[1], o1[1]) - min(o[1], o1[1])
    time = o1[0] - o[0]
    speed = distance / time
    maxSpeed = speed if speed > maxSpeed else maxSpeed
print(maxSpeed)