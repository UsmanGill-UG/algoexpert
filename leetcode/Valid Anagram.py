'''
  Question Number #
   
'''

def isAnagram(s, t):
    if len(s)!=len(t):
        return False
    result = [0 for i in range(27)]
    for i in range(len(s)):
        result[ord(s[i])-ord('a')] += 1
        result[ord(t[i])-ord('a')] -= 1
    for i in range(27):
        if result[i] != 0:
            return False
    return True


'''
    Complexity :
    
 
'''