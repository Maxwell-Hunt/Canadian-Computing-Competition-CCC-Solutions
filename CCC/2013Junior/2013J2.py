word = input()
letters = "IOSHZXN"
good = True
for char in word:
    if(not char in letters):
        good = False
        break
if(good):
    print("YES")
else:
    print("NO")