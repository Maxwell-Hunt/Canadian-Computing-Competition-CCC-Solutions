from operator import attrgetter
friends = []
existingNums = []

class Friend:
    def __init__(self, number):
        self.number = number
        self.waitTime = 0
        self.isWaiting = True
        self.totalWaitTime = 0

numActions = int(input())
for i in range(numActions):
    action = input().split(" ")
    action[1] = int(action[1])
    if(action[0] == "R"):
        if(not action[1] in existingNums):
            friends.append(Friend(action[1]))
            existingNums.append(action[1])
        else:
            for friend in friends:
                if(friend.number == action[1]):
                    friend.isWaiting = True
                    break
        
    if(action[0] == "W"):
        for friend in friends:
            if(friend.isWaiting):
                friend.waitTime += action[1] - 1
                friend.totalWaitTime += action[1] - 1
    elif(action[0] == "S"):
        for friend in friends:
            if(friend.number == action[1]):
                friend.waitTime = 0
                friend.isWaiting = False
                break
    if(action[0] != "W"):
        for friend in friends:
            if(friend.isWaiting):
                friend.waitTime += 1
                friend.totalWaitTime += 1

friends.sort(key=attrgetter('number'))
for friend in friends:
    if(friend.isWaiting):
        print(friend.number, -1)
    else:
        print(friend.number, friend.totalWaitTime)
