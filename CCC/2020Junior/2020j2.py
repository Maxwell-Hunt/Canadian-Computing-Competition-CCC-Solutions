P = int(input())
N = int(input())
R = int(input())
x = N
counter = 0
while(x <= P):
    x += N*R
    N *= R
    counter += 1
print(counter)