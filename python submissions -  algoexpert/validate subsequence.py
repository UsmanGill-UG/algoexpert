def isValidSubsequence(array, sequence):
    # Write your code here.
    j = 0
    for i in range(len(array)): # N steps # O(N)
        if array[i] == sequence[j]:
            j+=1
        if j == len(sequence):
            return True
    return False
