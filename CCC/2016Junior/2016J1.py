score = 0
for i in range(6):
    score += 1 if input() == "W" else 0
if(score == 0):
    print(-1)
elif(score < 3):
    print(3)
elif(score < 5):
    print(2)
else:
    print(1)