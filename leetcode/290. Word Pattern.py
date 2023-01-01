def wordPattern( p, s):
    s = s.split()
    if len(p)!=len(s):
        return False
    p2s, s2p = {}, {}
    for i in range(len(p)):
        if s[i] not in s2p:
            s2p[s[i]] = p[i]
        elif s2p[s[i]] != p[i]:
            return False
        if p[i] not in p2s:
            p2s[p[i]] = s[i]
        elif p2s[p[i]] != s[i]:
            return False
    return True


p = "abba"
s = "dog dog dog dog"
wordPattern(p,s)