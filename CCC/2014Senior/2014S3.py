numTests = int(input())
tests = []
for i in range(numTests):
    tests.append([])
    numTreats = int(input())
    for j in range(numTreats):
        tests[i].append(int(input()))
    tests[i].reverse()

def solve(test_):
    test = test_[:]
    currentNumber = 1
    stack = []
    while currentNumber != len(test_):
        if(test):
            if(test[0] == currentNumber):
                test = test[1:]
                currentNumber += 1
                continue
        if(stack):
            if(stack[-1] == currentNumber):
                stack = stack[:len(stack) - 1]
                currentNumber += 1
                continue
        if(test):
            stack.append(test[0])
            test = test[1:]
            continue
        return "N"
    return "Y"
    
[print(solve(test)) for test in tests]
