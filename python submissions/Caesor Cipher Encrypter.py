# Strings Green
# Time Complexity O(n) 
# Space Complexity O(n)
def caesarCipherEncryptor(string, key):
    newstr = []
    for i in range(len(string)):
        new = ord(string[i]) + key
        while new > 122:
            new -= 26
        a = chr(new)
        newstr.append(a)
    return "".join(newstr)

string="xyz"
key=2
print(caesarCipherEncryptor(string,key))