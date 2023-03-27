# N^3
def threeNumberSum_Ncube(array, targetSum):
    result=[]
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            for z in range(j+1,len(array)):
                if array[i]+array[j]+array[z] == targetSum:
                    result.append([array[i],array[j],array[z]])
    return result

# n^2 time
# 
def threeNumberSum(array, targetSum):
    triplets = []
    array.sort()   # NlogN
    for current_pointer in range(len(array)-2):
        left_pointer = current_pointer + 1
        right_pointer = len(array) - 1
        while left_pointer < right_pointer:
            currentSum = array[current_pointer] + array[left_pointer] + array[right_pointer]
            if currentSum == targetSum:
                triplets.append([array[current_pointer] , array[left_pointer] ,array[right_pointer]])
                left_pointer += 1
                right_pointer -= 1
            elif currentSum < targetSum:
                left_pointer+=1
            else:
                right_pointer-=1
    return triplets


array = [0, 1, 2, -4, -1]
targetSum = 0
print(threeNumberSum(array, targetSum))