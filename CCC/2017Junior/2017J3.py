start = list(map(int, input().split()))
end = list(map(int, input().split()))
numSteps = int(input())
distance = abs(end[1] - start[1]) + abs(end[0] - start[0])
if(numSteps < distance):
    print("N")
else:
    if(numSteps % 2 == distance % 2):
        print("Y")
    else:
        print("N")