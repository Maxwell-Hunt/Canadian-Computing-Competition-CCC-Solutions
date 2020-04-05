needle = input()
haystack = input()

total = 0
previous = False
used = []
for i in range(len(haystack) - len(needle) + 1):
    temp = list(needle)
    permutation = ""
    if not previous:
        for j in range(i, i + len(needle)):
            if haystack[j] not in temp:
                break
            else:
                temp.remove(haystack[j])
                permutation += haystack[j] 
        else:
            if permutation not in used:
                previous = True
                total += 1
                used.append(permutation)
    else:
        if haystack[i - 1] == haystack[i + len(needle) - 1]:
            if haystack[i:i+len(needle)] not in used:
                total += 1
            else:
                previous = False
                used.append("".join(haystack[i:i+len(needle)]))
print(total)