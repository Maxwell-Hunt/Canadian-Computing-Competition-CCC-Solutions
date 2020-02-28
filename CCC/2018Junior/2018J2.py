def J2(num,day1,day2):
    sum = 0  
    for i in range(num):
        if(day1[i] == day2[i]) and (day1[i] == "C"):
            sum += 1  
    return sum  

number = int(input())  
one = input()  
two = input()  

print(J2(number,one,two))  