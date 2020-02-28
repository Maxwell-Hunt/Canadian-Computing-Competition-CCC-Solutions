time = 1200
numMinutes = int(input())
def arithmaticSequence(num):
    L = list(map(int, list(str(num))))
    s = L[1] - L[0]
    for i in range(2, len(L)):
        if(L[i] - L[i - 1] != s):
            return False
    return True

total = 31 * int(numMinutes/720)
numMinutes -= int(numMinutes/720) * 720
for i in range(numMinutes):
    time += 1
    if(time % 100 == 60):
        if(time == 1260):
            time = 100
        else:
            time += 40
    if(arithmaticSequence(time)):
        
        total += 1
print(total)
    