numSymbols = int(input())
outputs = []
for i in range(numSymbols):
    data = input().split()
    outputs.append(int(data[0])*data[1])
for output in outputs:
    print(output)