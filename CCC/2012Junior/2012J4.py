from string import ascii_uppercase
letters = ascii_uppercase * 5
k = int(input())
word = input()
decoded = ""
for i in range(len(word)):
    p = i + 1
    positionInAlphabet = letters.find(word[i], 104)
    positionInAlphabet -= k
    positionInAlphabet -= 3 * p
    decoded += letters[positionInAlphabet]
print(decoded)