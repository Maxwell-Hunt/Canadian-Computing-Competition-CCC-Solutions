message = input()
happy = message.count(":-)")
sad = message.count(":-(")
if(happy > sad):
    print("happy")
elif(happy < sad):
    print("sad")
elif(happy == sad == 0):
    print("none")
else:
    print("unsure")
