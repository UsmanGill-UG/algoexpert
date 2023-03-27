# N^2 approach
# Two loops and keep track
# Ew

#   O(max of NlogN or MlogM)
# Sorting will take NlogN
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    a1p = 0
    a2p = 0
    smallest = float("inf")
    current_diff = float("inf")
    smallestPair = []
    while a1p< len(arrayOne) and a2p< len(arrayTwo):
        firstNum = arrayOne[a1p]
        secondNum = arrayTwo[a2p]
        if firstNum<secondNum:
            current_diff = secondNum-firstNum
            a1p+=1
        elif secondNum<firstNum:
            current_diff = firstNum-secondNum
            a2p+=1
        else:
            return [firstNum,secondNum]
        if smallest > current_diff:
            smallest = current_diff
            smallestPair = [firstNum, secondNum]
    return smallestPair
    

array1 = [-1, 5, 10, 20, 28, 3]
array2 = [26, 134, 135, 15, 17]
print(smallestDifference(array1,array2))
