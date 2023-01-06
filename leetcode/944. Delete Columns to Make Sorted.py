def minDeletionSize(strs):
    count = 0 
    for i in strs:
        a = ''.join(sorted(i))
        b = ''.join(sorted(i, reverse=True))
        if a != i and b!=i:
            count+=1
    return count


strs =["cba","daf","ghi"]
print(minDeletionSize(strs))