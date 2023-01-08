def twoNumberSum(array, targetSum):
    # Write your code here.
    #using hash map
    map ={}
    for i in array: # traverse through the array
        if targetSum - i in map: # if you find the solution
            return [i, targetSum-i] # return it
        else:
            map[i]= i # store it in the hashtable
    return []
