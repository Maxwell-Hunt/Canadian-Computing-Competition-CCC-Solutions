def distinct(num):
    for i, digit in enumerate(str(num)):
        if(str(num)[i:].count(digit) > 1):
            return False
    return True

currentYear = int(input()) + 1
while(not distinct(currentYear)): currentYear += 1
print(currentYear)