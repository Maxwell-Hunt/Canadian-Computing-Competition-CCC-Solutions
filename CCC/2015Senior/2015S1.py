numbers = []
for _ in range(int(input())):
    data = int(input())
    if(data == 0):
        numbers.pop()
    else:
        numbers.append(data)
print(sum(numbers))