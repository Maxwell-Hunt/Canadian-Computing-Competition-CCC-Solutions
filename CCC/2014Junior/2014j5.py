numStudents = int(input())
studentsA = input().split()
studentsB = input().split()
pairs = {}

def goodPair():
    for i in range(len(studentsA)):
        if(studentsB[i] in pairs):
            if(pairs[studentsB[i]] != studentsA[i]):
                return False
        if(studentsA[i] == studentsB[i]):
            return False
        pairs[studentsA[i]] = studentsB[i]
    return True

if(goodPair()):
    print("good")
else:
    print("bad")