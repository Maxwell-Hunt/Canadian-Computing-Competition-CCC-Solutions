gates = [True] * int(input())
planes = [int(input()) for _ in range(int(input()))]

total = 0
for plane in planes:
    docable = True
    while(not gates[plane - 1]):
        plane -= 1
        if(plane == 0):
            docable = False
            break
    if(docable):
        total += 1
        gates[plane - 1] = False
    else:
        break
    
print(total)