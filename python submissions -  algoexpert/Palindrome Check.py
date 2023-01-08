def isPalindrome(string):
    lp = 0
    rp = len(string)-1
    while lp -1 <= rp:
        if not string[lp] == string[rp]:
            return False
        lp += 1
        rp -= 1
    return True

#Time Complexity:  O(N)
#Space Complexity: O(1)

string ="abcdcba"

isPalindrome(string)