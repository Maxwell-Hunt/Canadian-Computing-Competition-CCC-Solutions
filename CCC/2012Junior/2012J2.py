depths = [int(input()) for i in range(4)]

def increasing(readings):
    for i in range(1, len(readings)):
        if(readings[i] > readings[i - 1]):
            continue
        return False
    return True

def decreasing(readings):
    for i in range(1, len(readings)):
        if(readings[i] < readings[i - 1]):
            continue
        return False
    return True

def same(readings):
    for i in range(1, len(readings)):
        if(readings[i] != readings[0]):
            return False
    return True

if(increasing(depths)):
    print("Fish Rising")
elif(decreasing(depths)):
    print("Fish Diving")
elif(same(depths)):
    print("Fish At Constant Depth")
else:
    print("No Fish")