numInputs = int(input())
data = []
for _ in range(numInputs):
    data.append(input())

for message in data:
    while(len(message) > 0):
        currentSymbol = message[0]
        numTimes = 0
        i = 0
        while(i < len(message) and message[i] == currentSymbol):
            i += 1
        print(i, currentSymbol, end=" ")
        message = message[i:]
    print()
    
