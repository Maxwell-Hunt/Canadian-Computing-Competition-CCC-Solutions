speedLimit = int(input("Enter the speed limit: "))
speed = int(input("Enter the recorded speed of the car: "))

if(speed > speedLimit):
    x = speed - speedLimit
    if(x < 21):
        print("You are speeding and your fine is $100.")
    elif(x < 31):
        print("You are speeding and your fine is $270.")
    else:
        print("You are speeding and your fine is $500.")
else:
    print("Congratulations, you are within the speed limit!")