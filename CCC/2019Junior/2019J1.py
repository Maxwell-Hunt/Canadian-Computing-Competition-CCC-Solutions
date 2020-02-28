a3 = int(input())*3
a2 = int(input())*2
a1 = int(input())
b3 = int(input())*3
b2 = int(input())*2
b1 = int(input())
a = a3+a2+a1
b = b3+b2+b1
if(a > b):
    print("A")
elif(a == b):
    print("T")
else:
    print("B")