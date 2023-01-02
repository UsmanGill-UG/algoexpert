def detectCapitalUse(word):
    return len(word)==1 or word[1:].islower() or word.isupper()

    
word  ="FFf"
print(detectCapitalUse(word))