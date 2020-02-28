def distinct(year):
    sYear = str(year)
    chars = ""
    for digit in sYear:
        if(digit in chars):
            return False
        chars += digit
    return True

currentYear = int(input())
currentYear += 1
while(not distinct(currentYear)):
    currentYear += 1
print(currentYear)