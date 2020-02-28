from string import ascii_letters
letters = ascii_letters[:26]
vowels = "aeiou"
word = input()
newWord = ""
for c in word:
    newWord += c
    if(c not in vowels):
        closestVowel = ""
        closestDist = 27
        cp = letters.find(c)
        for v in vowels:
            cv = letters.find(v)
            if(abs(cv - cp) < closestDist):
                closestDist = abs(cv-cp)
                closestVowel = v
        newWord += closestVowel
        if(c == "z"):
            newWord += "z"
        else:
            cp += 1
            while(letters[cp] in vowels):
                cp += 1
            newWord += letters[cp]
        
print(newWord)
