def isPalindrome(s):
    x = list(s)
    y = x[:]
    y.reverse()
    if(x == y):
        return True
    return False

word = input()
longest = 0
for i in range(len(word)):
    for j in range(i, len(word)+1):
        if(isPalindrome(word[i:j])):
            if(len(word[i:j]) > longest):
                longest = len(word[i:j])
print(longest)