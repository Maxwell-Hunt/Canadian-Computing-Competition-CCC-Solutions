rows = [0,
        0,
        0,
        0]
cols =    [0,0,0,0]


for i in range(4):
    data = list(map(int,input().split()))
    for j in range(len(data)):
        rows[i] += data[j]
        cols[j] += data[j]

def same(arr):
    for i in range(1, len(arr)):
        if(arr[i] != arr[0]):
            return False
    return arr[0]

if(same(rows) and same(rows) == same(cols)):
    print("magic")
else:
    print("not magic")