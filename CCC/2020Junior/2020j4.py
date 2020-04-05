mainString = input()
possibleSub = input()

def getCyclicShifts(s):
    arr = []
    for i in range(len(s)):
        arr.append(s)
        f = s[0]
        s = s[1:]
        s += f
    return arr

shifts = getCyclicShifts(possibleSub)
for shift in shifts:
    if(shift in mainString):
        print("yes")
        break
else:
    print("no")